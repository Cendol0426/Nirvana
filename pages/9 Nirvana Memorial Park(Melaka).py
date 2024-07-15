import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.header("Melaka Nirvana Memorial Park")
st.header("马六甲富贵山庄")
st.write("since 2019")
image1 = Image.open("image2/melaka1.png")
st.image(image1.resize((1000, 500)))
image2 = Image.open("image2/melaka2.png")
st.image(image2.resize((1000, 500)))
image3 = Image.open("image2/melaka3.png")
st.image(image3.resize((1000, 500)))

st.header("  ")
st.header("  ")

number = st.slider("请滑动来观看更多资讯与照片 Pictures and Info, Please Slide to view", 1, 3, key="burial")
slidingimage = ["image2/melaka4", "image2/melaka5", "image2/melaka6"]
image4 = Image.open(slidingimage[number - 1] + ".png")
st.image(image4.resize((1000, 500)))

st.header("  ")
st.header("  ")

number1 = st.slider("请滑动来观看更多资讯与照片 Pictures and Info, Please Slide to view", 1, 3, key="cremation")
slidingimage1 = ["image2/melaka7", "image2/melaka8", "image2/melaka9"]
image4 = Image.open(slidingimage1[number1 - 1] + ".png")
st.image(image4.resize((1000, 500)))