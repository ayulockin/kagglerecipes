# Kaggle Recipes



![kaggle_wandb.png](nbs\data\images\kaggle_wandb.png)

## What's New

#### Sept 2, 2021
- Release version 0.0.3
- Added support for multiprocessing to extract DICOM metadata for RSNA-MICCAI Brain Tumor Classification competition.
- Bug fixes. 

#### Aug 27, 2021
- Released the library on PyPI.
- Easily create voxel manipulated dataset for RSNA-MICCAI Brain Tumor Classification competition. 
- Extract dicom metadata. 
- Added utilities to log dataframe as tables and files/directory as artifacts. 
- Added utiities to log basic W&B charts (line, bar, and scatter).

## Kaggle Competitions
- [RSNA-MICCAI Brain Tumor Radiogenomic Classification](https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification)

## Code & Scripts

#### RSNA-MICCAI Brain Tumor Radiogenomic Classification
- LINK TO NOTEBOOK

## Install

`pip install kagglerecipes`

## Sample Datasets 

We have also logged smaller subsets of Kaggle commpeition datasets local development and fast prototyping. 

#### RSNA-MICCAI Brain Tumor Radiogenomic Classification
* Download it manually from [here](https://wandb.ai/wandb_fc/rsna-miccai-brain/artifacts/dataset/sample/0c38392ee79fd5f85e97/files).
* Or download it using this code snippet.
  ```
  import wandb
  run = wandb.init()
  artifact = run.use_artifact('wandb_fc/rsna-miccai-brain/sample:v0', type='dataset')
  artifact_dir = artifact.download()
  ```

## Credits

The code in this repository is a combination of many of the Kagglers' work that they have shared publicly as Kaggle kernels.

* [Connecting voxel spaces](https://www.kaggle.com/boojum/connecting-voxel-spaces) by [Michael Beregov](https://www.kaggle.com/boojum)
* [Normalized Voxels: Align Planes and Crop](https://www.kaggle.com/ren4yu/normalized-voxels-align-planes-and-crop) by [yu4u](https://www.kaggle.com/ren4yu)
* [DICOM to 2D Resized Axial PNGs 256x256 [x36]](https://www.kaggle.com/smoschou55/dicom-to-2d-resized-axial-pngs-256x256-x36) by [Sofia Moschou](https://www.kaggle.com/smoschou55)
