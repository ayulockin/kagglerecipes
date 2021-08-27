# Kaggle Recipes



![kaggle_wandb.png](nbs\data\images\kaggle_wandb.png)

## What's New
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
