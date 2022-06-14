## Changelog

### v0.2.3 (13/06/2022)

#### Highlight
* Provide README in [configs](https://github.com/Westlake-AI/openmixup/tree/main/configs/benchmarks/classification/) for self-supervised learning methods based on MMSelfSup.
* Support new Masked Image Modeling (MIM) methods ([A2MIM](https://arxiv.org/abs/2205.13943), [CAE](https://arxiv.org/abs/2202.03026)).
* Support new Fine-tuing method ([HCR](https://arxiv.org/abs/2206.00845)).
* Support new mixup augmentation methods ([SmoothMix](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w45/Lee_SmoothMix_A_Simple_Yet_Effective_Data_Augmentation_to_Train_Robust_CVPRW_2020_paper.pdf), [GridMix](https://www.sciencedirect.com/science/article/pii/S0031320320303976)).
* Support more regression losses ([Focal L1/L2 loss](https://arxiv.org/abs/2102.09554), [Balanced L1 loss](https://arxiv.org/abs/1904.02701), [Balanced MSE loss](https://arxiv.org/abs/2203.16427)).
* Support more regression metrics (regression errors and correlations) and the regression dataset.
* Support more reweight classification losses ([Gradient Harmonized loss](https://arxiv.org/abs/1811.05181), [Varifocal Focal Loss](https://arxiv.org/abs/1811.05181)) from [MMDetection](https://github.com/open-mmlab/mmdetection). 

### v0.2.2 (24/05/2022)

#### Highlight
* Support more self-supervised methods (Barlow Twins and Masked Image Modeling methods).
* Support popular backbones (ConvMixer, MLPMixer, VAN) based on MMClassification.
* Support more regression losses (Charbonnier loss and Focal Frequency loss).

### Bug Fixes
* Fix bugs in self-supervised classification benchmarks (configs and implementations of VisionTransformer).
* Update [INSTALL.md](INSTALL.md). We suggest you install **PyTorch 1.8** or higher and mmcv-full for better usage of this repo. **PyTorch 1.8** has bugs in AdamW optimizer.
* Fix bugs in PreciseBNHook (update all BN stats) and RepeatSampler (set sync_random_seed).

### v0.2.1 (19/04/2022)

#### Highlight
* Support masked image modeling (MIM) self-supervised methods (MAE, SimMIM, MaskFeat).
* Support visualization of reconstruction results in MIM methods.
* Support basic regression losses and metrics.

### Bug Fixes
* Fix bugs in regression metrics, MIM dataset, and benchmark configs. Notice that only `l1_loss` is supported by FP16 training, other regression losses (e.g., MSE and Smooth_L1 losses) will cause NAN when the target and prediction are not normalized in FP16 training.
* We suggest you install **PyTorch 1.8** or higher (required by some self-supervised methods) and mmcv-full for better usage of this repo. You can still use **PyTorch 1.6** for supervised classification methods.

### v0.2.0 (31/03/2022)

#### Highlight
* Support various popular backbones (ConvNets and ViTs), various image datasets, popular mixup methods, and benchmarks for supervised learning. Config files are available.
* Support popular self-supervised methods (e.g., BYOL, MoCo.V3, MAE) on both large-scale and small-scale datasets, and self-supervised benchmarks (merged from MMSelfSup). Config files are available.
* Support analyzing tools for self-supervised learning (kNN/SVM/linear metrics and t-SNE/UMAP visualization).
* Convenient usage of configs: fast configs generation by 'auto_train.py' and configs inheriting (MMCV).
* Support mixed-precision training (NVIDIA Apex or MMCV Apex) for all methods.
* [Model Zoos](docs/model_zoos) and lists of [Awesome Mixups](docs/awesome_mixups) have been released.

#### Bug Fixes
* Done code refactoring follows MMSelfSup and MMClassification.

### v0.1.3 (25/03/2022)

* Refactor code structures for vision transformers and self-supervised methods (e.g., MoCo.V3 and MAE).
* Provide online analysis of self-supervised methods (knn metric and t-SNE/UMAP visualization). 
* More results are provided in Model Zoos.

#### Bug Fixes
* Fix bugs of reusing of configs, ViTs, visualization tools, etc. It requires rebuilding of OpenMixup (install mmcv-full).

### v0.1.2 (20/03/2022)

#### Highlight
* Refactor code structures according to MMSelfsup to fit high version of mmcv and PyTorch.
* Support self-supervised methods and optimizes config structures.

### v0.1.1 (15/03/2022)

#### Highlight
* Support various popular backbones (ConvNets and ViTs).
* Support various handcrafted methods and optimization-based methods (e.g., [PuzzleMix](https://arxiv.org/abs/2009.06962), [AutoMix](https://arxiv.org/pdf/2103.13027), [SAMix](https://arxiv.org/pdf/2111.15454), etc.).
* Provide supervised image classification benchmarks in model_zoo and results (on updating). 

#### Bug Fixes
* Fix bugs of new mixup methods (e.g., gco for Puzzlemix, etc.).

### v0.1.0 (22/01/2022)

#### Highlight
* Support various popular backbones (popular ConvNets and ViTs).
* Support mixed precision training (NVIDIA Apex or MMCV Apex).
* Support supervised, self- & semi-supervised learning methods and benchmarks.
* Support fast configs generation from a basic config file by 'auto_train.py'. 

#### Bug Fixes
* Fix bugs of code refactoring (backbones, fp16, etc.).

#### OpenSelfSup (v0.3.0, 14/10/2020) Supported Features

* Mixed Precision Training (NVIDIA Apex).
* Improvement of GaussianBlur doubles the training speed of MoCo V2, SimCLR, BYOL.
* More benchmarking results, including Places, VOC, COCO, linear/semi-supevised benchmarks.
* Fix bugs in moco v2 and byol, now the results are reproducible.
* Provide benchmarking results and model download links.
* Support updating network every several interations (accumulation).
* Support LARS and LAMB optimizer with nesterov (LAMB from MMclassification).
* Support excluding specific parameters from optimizer updation.