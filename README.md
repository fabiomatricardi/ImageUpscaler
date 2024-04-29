# ImageUpscaler


Streamlit App to Upscale images and compared visualization - Repo of the code from the Medium article 

This app leverage the amazing Repository [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN)

you can find it also on HuggingFace - https://huggingface.co/ai-forever/Real-ESRGAN

I tried to use also x2_Upscaler and x8_Upscaler but I always get an error from pytorch


1. you upload a picture
2. you generate the Upscaled image
3. you compare the results

<img src="https://github.com/fabiomatricardi/ImageUpscaler/raw/main/STAPP_Upscaler_Running_000.png" width=900>

> **NOTE**<br>
> The bigger the original image, the longer the Upscale time

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

<img src="https://github.com/fabiomatricardi/ImageUpscaler/raw/main/HuggingFaceRepo.png" width=700>

Download RealESRGAN_x4.pth into `weights` subfolder


### Run the stapp

from the terminal, with the venv still activated, run
```
python -m streamlit run .\stUpscaler4x.py
```

Note: original Image of Remo Williams from [here](https://www.hometheaterforum.com/wp-content/uploads/2016/10/remowilliamtop.jpg)


#### Other examples

<img src="https://github.com/fabiomatricardi/ImageUpscaler/raw/main/STAPP_Upscaler_Running.png" height=280><img src="https://github.com/fabiomatricardi/ImageUpscaler/raw/main/STAPP_Upscaler_Running1.png" height=280>
