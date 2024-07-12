import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
image7 = Image.open("image/image7.png")
st.image(image7.resize((720, 360)))
image8 = Image.open("image/image8.png")
st.image(image8.resize((720, 360)))
image9 = Image.open("image/image9.png")
st.image(image9.resize((720, 360)))