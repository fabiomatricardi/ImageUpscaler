import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
import torch
import numpy as np
from RealESRGAN import RealESRGAN
import datetime
import random
import string
import datetime

def genRANstring(n):
    """
    n = int number of char to randomize
    """
    N = n
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return res

@st.cache_resource 
def create_chain():   
    modelname = 'RealESRGAN_x4' #'RealESRGAN_x4plus'
    modelpath = f'weights/{modelname}.pth'
    print(f'Loading Upscaler model {modelname}')
    start = datetime.datetime.now()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model = RealESRGAN(device, scale=4)
    model.load_weights(modelpath, download=False)
    delta = datetime.datetime.now() - start
    print(f'Model loaded in {delta}')

    return model

if "gentime" not in st.session_state:
    st.session_state.gentime = "**:green[none yet]**"

def main():

    st.set_page_config(layout="wide", page_title="Image Comparison APP")
    model = create_chain()
    st.write("# 🌇🏙️ Compare two images")

    st.sidebar.write("## Upload the image to UPSCALE and compare :gear:")
    file1=None
    file2=None
    upscale_btn = st.button('Start 4x Upscale', type='primary')

    # Upload the images
    file1 = st.sidebar.file_uploader("Upload image 1", type=["png", "jpg", "jpeg"],accept_multiple_files=False)
    gentimetext = st.sidebar.empty()
    #file2 = st.sidebar.file_uploader("Upload image 2", type=["png", "jpg", "jpeg"],accept_multiple_files=False)

    if (upscale_btn and file1):
        with st.spinner("Upscaling..."):
            start = datetime.datetime.now()
            image = Image.open(file1).convert('RGB')
            sr_image = model.predict(image, batch_size=1)
            savedName = f'upscaled_{genRANstring(4)}.png'
            sr_image.save(savedName)
            file2 = savedName
            delta = datetime.datetime.now() - start
            st.session_state.gentime = f"**:green[{str(delta)}]**"
            gentimetext.write(st.session_state.gentime)
            st.success('Image Upscaled and Saved')
    if  not file1:
        st.warning("Upload a low quality image to run Upscaler!")
            
    
    filename_1, filename_2 = st.columns([1, 1])


    if file1 and file2:
        img1 = Image.open(file1)
        img2 = Image.open(file2)
        
        ## Display filename
        with filename_1: st.write(f"### Image 1: {file1.name}")
        with filename_2: st.write(f"### Image 2: {file2}")

        ## Display image
        image_comparison(img1,img2,label1="ORIGINAL",label2="4x UPSCALED",width=1100)
    else:
        st.warning("Run Upscaler before Comparison is possible")

if __name__ == "__main__":
    main()