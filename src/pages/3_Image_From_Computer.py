import streamlit as st
import cv2
import numpy as np
import cv2
from io import StringIO
from image_emotion_gender_demo import classification_image
import time


st.title("Classification Image from File")

st.markdown("""
               ###
               1. Pilih Browse File pada kolom yang tersedia 
               2. Pilih Foto yang ingin di klasifikasi
               3. Tunggu hingga hasil proses gambar
              """)


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    progress_text = "Processing image..."
    my_bar = st.progress(0)

    img_classificated = classification_image(cv2_img)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    st.image(img_classificated, caption='Result')