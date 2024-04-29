# ImageUpscaler


Streamlit App to Upscale images and compared visualization - Repo of the code from the Medium article 

This app leverage the amazing Repository [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN)

you can find it also on HuggingFace - https://huggingface.co/ai-forever/Real-ESRGAN

I tried to use also x2_Upscaler and x8_Upscaler but I always get an error from pytorch


1. you upload a picture
2. you generate the Upscaled image
3. you compare the results


## Requirements

#### create a virtual environment
```
python -m venv venv
venv\Scripts\activate
```

#### Install the PIP dependencies
```
pip install git+https://github.com/sberbank-ai/Real-ESRGAN.git
pip install streamlit
pip install streamlit-image-comparison
```

#### Download the pytorch weigths

from https://huggingface.co/ai-forever/Real-ESRGAN

Download RealESRGAN_x4.pth into `weights` subfolder


### Run the stapp

from the terminal, with the venv still activated, run
```
python -m streamlit run .\stUpscaler4x.py
```
