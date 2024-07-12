import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.header("Kulai Nirvana Memorial Park")
st.header("古来富贵山庄")
st.subheader("since 2000")
image1 = Image.open("image/kulai5.png")
st.image(image1.resize((720, 360)))
image2 = Image.open("image/kulai6.png")
st.image(image2.resize((720, 360)))
image3 = Image.open("image/kulai7.png")
st.image(image3.resize((720, 360)))

col1, emptycol1, col2 = st.columns((2,0.4, 2))
with col1:
    image4 = Image.open("image/kulai8.png")
    st.image(image4.resize((720, 360)))
    image5 = Image.open("image/kulai9.png")
    st.image(image5.resize((720, 360)))
    image6 = Image.open("image/kulai10.png")
    st.image(image6.resize((720, 360)))
    image7 = Image.open("image/kulai11.png")
    st.image(image7.resize((720, 360)))

with col2:
    image8 = Image.open("image/kulai12.png")
    st.image(image8.resize((720, 360)))
    image9 = Image.open("image/kulai13.png")
    st.image(image9.resize((720, 360)))
    image10 = Image.open("image/kulai14.png")
    st.image(image10.resize((720, 360)))
    image11 = Image.open("image/kulai15.png")
    st.image(image11.resize((720, 360)))