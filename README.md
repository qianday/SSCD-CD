# Summator-Subtractor Network: Modeling spatialand channel differences for Change Detection

Here, we provide the pytorch implementation of the paper: Summator-Subtractor Network: Modeling spatial
and channel differences for Change Detection.

For more ore information, please see our published paper at [IEEE TGRS](https://ieeexplore.ieee.org/document/9491802) or [arxiv](https://arxiv.org/abs/2103.00208). 

![image](./images/SSCD.png)

## Requirements

```
Python 3.8.2
pytorch 1.10.1
torchvision 0.11.2
einops  0.6.1
```

## Train

You can find the training script `run_cd.sh` in the folder `scripts`. You can run the script file by `sh scripts/run_cd.sh` in the command environment.

The detailed script file `run_cd.sh` is as follows:

```cmd
gpus=0
checkpoint_root=checkpoints 
data_name=LEVIR  # dataset name 

img_size=256
batch_size=8
lr=0.01
max_epochs=200  #training epochs
net_G=base_transformer_pos_s4_dd8 # model name
lr_policy=linear

split_train=train  # training txt
split_val=val  #validation txt
project_name=CD_${net_G}_${data_name}_b${batch_size}_lr${lr}_${split}_${split_val}_${max_epochs}_${lr_policy}

python main_cd.py --img_size ${img_size} --checkpoint_root ${checkpoint_root} --lr_policy ${lr_policy} --split ${split} --split_val ${split_val} --net_G ${net_G} --gpu_ids ${gpus} --max_epochs ${max_epochs} --project_name ${project_name} --batch_size ${batch_size} --data_name ${data_name}  --lr ${lr}
```

## Evaluate

You can find the evaluation script `eval.sh` in the folder `scripts`. You can run the script file by `sh scripts/eval.sh` in the command environment.

The detailed script file `eval.sh` is as follows:

```cmd
gpus=0
data_name=LEVIR # dataset name
net_G=base_transformer_pos_s4_dd8_dedim8 # model name 
split=test # test.txt
project_name=BIT_LEVIR # the name of the subfolder in the checkpoints folder 
checkpoint_name=best_ckpt.pt # the name of evaluated model file 

python eval_cd.py --split ${split} --net_G ${net_G} --checkpoint_name ${checkpoint_name} --gpu_ids ${gpus} --project_name ${project_name} --data_name ${data_name}
```

## Dataset Preparation

### Data structure

```
"""
Change detection data set with pixel-level binary labels；
├─A
├─B
├─label
└─list
"""
```

`A`: images of t1 phase;

`B`:images of t2 phase;

`label`: label maps;

`list`: contains `train.txt, val.txt and test.txt`, each file records the image names (XXX.png) in the change detection dataset.

### Data Download 

LEVIR-CD: https://justchenhao.github.io/LEVIR/

WHU-CD: https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html

DSIFN-CD: https://github.com/GeoZcx/A-deeply-supervised-image-fusion-network-for-change-detection-in-remote-sensing-images/tree/master/dataset

## Citation

If you use this code for your research, please cite our paper:

```
@ARTICLE{10380600,
  author={Wang, Leiquan and Fang, Ye and Li, Zhongwei and Wu, Chunlei and Xu, Mingming and Shao, Mingwen},
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  title={Summator–Subtractor Network: Modeling Spatial and Channel Differences for Change Detection}, 
  year={2024},
  volume={62},
  number={},
  pages={1-12},
  doi={10.1109/TGRS.2024.3349638}}
```