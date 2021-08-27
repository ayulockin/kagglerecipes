# 🥇 Kaggle Recipes 🥇
> Helpful data preprocessing, training and visualisatoin code and scripts for a range Kaggle competitions, supported by Weights & Biases. Less spaghetti code, more visualisation -> better results


![kaggle_wandb.png](nbs/data/images/kaggle_wandb.png)

## What's New
#### Aug 27, 2021
- Adds X,Y,Z

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

# Sample Dataset 

We are using a subset of dataset for local development and fast prototyping. 

* Download it manually from [here](https://wandb.ai/wandb_fc/rsna-miccai-brain/artifacts/dataset/sample/0c38392ee79fd5f85e97/files).
* Or download it using this code snippet.

  ```
  import wandb
  run = wandb.init()
  artifact = run.use_artifact('wandb_fc/rsna-miccai-brain/sample:v0', type='dataset')
  artifact_dir = artifact.download()
  ```
