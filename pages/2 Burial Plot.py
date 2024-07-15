import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("福地, Burial Plot")
image3 = Image.open("image/image3.png")
st.image(image3.resize((1000, 500)))

number = st.slider("请滑动来观看更多资讯与照片 Pictures and Info, Please Slide to view", 1, 3)

slidingimage = ["image/kulai25", "image/image4", "image/image5", "image/image6"]
image2 = Image.open(slidingimage[number - 1] + ".png")
st.image(image2.resize((1000, 500)))