_base_ = [
    '../_base_/models/swin-base.py',
    '../_base_/datasets/imagenet_swin_ft_sz192_8xbs128.py',
    '../_base_/default_runtime.py',
]

# data
data = dict(imgs_per_gpu=32, workers_per_gpu=6)

# interval for accumulate gradient
update_interval = 8  # total: 8 x bs32 x 8 accumulates = bs2048

# optimizer
optimizer = dict(
    type='AdamW',
    lr=1.25e-3 * 2048 / 512,
    weight_decay=0.05, eps=1e-8, betas=(0.9, 0.999),
    paramwise_options={
        '(bn|ln|gn)(\d+)?.(weight|bias)': dict(weight_decay=0.),
        'bias': dict(weight_decay=0.),
        'absolute_pos_embed': dict(weight_decay=0.),
        'relative_position_bias_table': dict(weight_decay=0.),
    },
    constructor='TransformerFinetuneConstructor',
    model_type='swin',
    layer_decay=0.9)

# apex
use_fp16 = True
fp16 = dict(type='apex', loss_scale=dict(init_scale=512., mode='dynamic'))
# optimizer args
optimizer_config = dict(
    update_interval=update_interval, use_fp16=use_fp16,
    grad_clip=dict(max_norm=5.0),
)

# learning policy
lr_config = dict(
    policy='CosineAnnealing',
    min_lr=2.5e-7 * 2048 / 512,
    warmup='linear',
    warmup_iters=20,
    warmup_ratio=2.5e-7 / 1.25e-3,
    warmup_by_epoch=True,
    by_epoch=False)

# runtime settings
runner = dict(type='EpochBasedRunner', max_epochs=100)