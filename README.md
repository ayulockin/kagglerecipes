# Kaggle RSNA-MICCAI Brain Tumor
> Useful code and scripts for the RSNA-MICCAI Brain Tumor Radiogenomic Classification Kaggle competition


This file will become your README and also the index of your documentation.

## Install

`pip install brain_tumor`

## Library Structure:
- data
- utils
- preprocess
- postprocess
- viz
- train

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

## How to use

Fill me in please! Don't forget code examples:

```
# 1+1
```




    2


