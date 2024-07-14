import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("福地, Burial Plot")
image3 = Image.open("image/image3.png")
st.image(image3.resize((720, 360)))
image4 = Image.open("image/image4.png")
st.image(image4.resize((720, 360)))
image5 = Image.open("image/image5.png")
st.image(image5.resize((720, 360)))
image6 = Image.open("image/image6.png")
st.image(image6.resize((720, 360)))