from streamlit_lottie import st_lottie
import requests
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# fungsi lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Pengaturan halaman
st.set_page_config(
    page_title="Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Fungsi untuk setiap halaman
def homepage():
    st.markdown("""
    <style>
        .main {
            background-color: #eeeeee;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            color: #4a4a4a;
        }
        .stButton button {
            background-color: #5a5a5a;
            color: white;
        }
        .info-box {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #999999;
            margin-bottom: 20px;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
