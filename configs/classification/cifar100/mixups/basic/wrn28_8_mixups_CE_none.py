_base_ = '../../../../base.py'
# model settings
model = dict(
    type='MixUpClassification',
    pretrained=None,
    alpha=1,
    mix_mode="mixup",
    mix_args=dict(
        attentivemix=dict(grid_size=32, top_k=None, beta=8),  # AttentiveMix+ in this repo (use pre-trained)
        automix=dict(mask_adjust=0, lam_margin=0),  # require pre-trained mixblock
        fmix=dict(decay_power=3, size=(32,32), max_soft=0., reformulate=False),
        manifoldmix=dict(layer=(0, 3)),
        puzzlemix=dict(transport=True, t_batch_size=None, t_size=4,  # t_size for small-scale datasets
            block_num=5, beta=1.2, gamma=0.5, eta=0.2, neigh_size=4, n_labels=3, t_eps=0.8),
        resizemix=dict(scope=(0.1, 0.8), use_alpha=True),
        samix=dict(mask_adjust=0, lam_margin=0.08),  # require pre-trained mixblock
    ),
    backbone=dict(
        # type='WideResNet',  # normal
        type='WideResNet_Mix',  # required by 'manifoldmix'
        first_stride=1,  # CIFAR version
        in_channels=3,
        depth=28, widen_factor=8,  # WRN-28-8, 128-256-512
        drop_rate=0.0,
        out_indices=(2,),  # no conv-1, x-1: stage-x
        frozen_stages=-1,
    ),
    head=dict(
        type='ClsHead',  # normal CE loss (NOT SUPPORT PuzzleMix, use soft/sigm CE instead)
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        with_avg_pool=True, multi_label=False, in_channels=512, num_classes=100)
)
# dataset settings
data_source_cfg = dict(type='CIFAR100', root='data/cifar100/')
dataset_type = 'ClassificationDataset'
img_norm_cfg = dict(mean=[0.4914, 0.4822, 0.4465], std=[0.2023, 0.1994, 0.201])
train_pipeline = [
    dict(type='RandomCrop', size=32, padding=4, padding_mode="reflect"),
    dict(type='RandomHorizontalFlip'),
]
test_pipeline = []
# prefetch
prefetch = True
if not prefetch:
    train_pipeline.extend([dict(type='ToTensor'), dict(type='Normalize', **img_norm_cfg)])
test_pipeline.extend([dict(type='ToTensor'), dict(type='Normalize', **img_norm_cfg)])

data = dict(
    imgs_per_gpu=100,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_source=dict(split='train', **data_source_cfg),
        pipeline=train_pipeline,
        prefetch=prefetch,
    ),
    val=dict(
        type=dataset_type,
        data_source=dict(split='test', **data_source_cfg),
        pipeline=test_pipeline,
        prefetch=False),
)

# additional hooks
custom_hooks = [
    dict(
        type='ValidateHook',
        dataset=data['val'],
        initial=False,
        interval=1,
        imgs_per_gpu=100,
        workers_per_gpu=4,
        eval_param=dict(topk=(1, 5)))
]

# optimizer
optimizer = dict(type='SGD',
                 lr=0.03, momentum=0.9, weight_decay=0.001)  # adjust wd={1e-3, 5e-4} for mixup methods
# apex
use_fp16 = False
optimizer_config = dict(update_interval=1, use_fp16=use_fp16, grad_clip=None)

# learning policy
lr_config = dict(policy='CosineAnnealing', min_lr=0.)
checkpoint_config = dict(interval=800)

# runtime settings
total_epochs = 400
