# Ref-Gaussian: Reflective Gaussian Splatting
### [[Project]](https://fudan-zvg.github.io/ref-gaussian) [[Paper]](https://arxiv.org/abs/2412.19282)

> [**Reflective Gaussian Splatting**](https://arxiv.org/abs/2412.19282),            
> [Yuxuan Yao](https://yaoyuxuanyyds.github.io/), Zixuan Zeng, [Chun Gu](https://sulvxiangxin.github.io/), [Xiatian Zhu](https://surrey-uplab.github.io/), [Li Zhang](https://lzrobots.github.io)  
> **ICLR 2025**

**Official implementation of "Reflective Gaussian Splatting".** 

## 🎥 Video

https://github.com/user-attachments/assets/99a9b449-f7b0-4db0-8f97-2ce5a5f5639d


## 🛠️ Pipeline
<div align="center">
  <img src="assets/pipeline.png"/>
</div><br/>



## ⚙️ Get started
### Installation
```bash
# clone the repo
git clone https://github.com/fudan-zvg/ref-gaussian.git --recursive
cd ref-gaussian
# create conda environment
conda create -n ref-gaussian python=3.9
conda activate ref-gaussian

# install pytorch (e.g. cuda 12.6)
pip3 install torch==2.7.1+cu126 torchvision --index-url https://download.pytorch.org/whl/cu126
# install submodules
pip install submodules/cubemapencoder --no-build-isolation
pip install submodules/diff-surfel-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation
pip install submodules/raytracing --no-build-isolation

# install other denpendencies
pip install -r requirements.txt
```


### Dateset
We mainly test our method on [Shiny Blender Synthetic](https://storage.googleapis.com/gresearch/refraw360/ref.zip), [Shiny Blender Real](https://storage.googleapis.com/gresearch/refraw360/ref_real.zip), [Glossy Synthetic](https://liuyuan-pal.github.io/NeRO/) and [NeRF Synthetic dataset](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1). Please run the script `nero2blender.py` to convert the format of the Glossy Synthetic dataset.


###  Running
We provide the script to test our code on each scene of datasets. Just run:
```
sh train.sh
```
You may need to modify the path in `train.sh`

<details>
<summary><span style="font-weight: bold;">Command Line Arguments for train.py</span></summary>

  #### --iteration
  The number of total iteration for training.

  #### --lambda_normal_smooth 
  The strength of normal smooth loss.
  
</details>
<br>

### Evaluation
```
python eval.py --white_background --save_images --model_path output/NAME_OF_THE_SCENE
```
You will get PSNR/SSIM/LPIPS/FPS results.



## Acknowledgement

This work is built on many amazing research works:

- [3DGS-DR](https://github.com/gapszju/3DGS-DR)
- [2DGS](https://github.com/hbb1/2d-gaussian-splatting)
- [Raytracing](https://github.com/ashawkey/raytracing)



## 📜 BibTeX
```bibtex
@inproceedings{yao2025refGS,
  title={Reflective Gaussian Splatting},
  author={Yao, Yuxuan and Zeng, Zixuan and Gu, Chun and Zhu, Xiatian and Zhang, Li},
  booktitle={ICLR},
  year={2025},
}
```
