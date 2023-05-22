import streamlit as st
import cv2
import numpy as np
from image_emotion_gender_demo import classification_image
from io import StringIO
import time


st.title("Classification Image from taking Photo")

st.markdown("""
               ###
               1. Nyalakan Kamera/Allow bila diperlukan

               2. Pilih Take Foto pada bagian bawah Foto

               3. Tunggu hingga hasil proses gambar
              """)



img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    progress_text = "Processing image..."
    my_bar = st.progress(0)

    img_classificated = classification_image(cv2_img)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)
    st.image(img_classificated, caption='Result')

