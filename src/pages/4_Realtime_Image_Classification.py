import streamlit as st
from video_emotion_gender_demo import RealtimeClassification
import time


st.title("Classification Image from RealTime Camera")

st.markdown("""
               ###
               1. Pilih Realtime Classification yang ditampilkan
               2. Pilih Foto yang ingin di klasifikasi
               3. Tunggu hingga hasil proses gambar
              """)


def run_realtime_classification():
    RealtimeClassification()

if st.button("Run Realtime Classification"):
    st.text("CLICK 'Q' KEY TO STOP")
    run_realtime_classification()