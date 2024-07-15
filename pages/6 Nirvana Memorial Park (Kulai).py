import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.header("Kulai Nirvana Memorial Park")
st.header("古来富贵山庄")
st.write("since 2000")
image = Image.open("image/kulai26.png")
st.image(image.resize((1000, 500)))
image1 = Image.open("image/kulai5.png")
st.image(image1.resize((1000, 500)))
image2 = Image.open("image/kulai6.png")
st.image(image2.resize((1000, 500)))
image3 = Image.open("image/kulai7.png")
st.image(image3.resize((1000, 500)))
st.header("  ")
st.header("  ")

number = st.slider("请滑动来观看更多资讯与照片 Pictures and Info, Please Slide to view", 1, 4, key="burial")
slidingimage = ["image/kulai8", "image/kulai9", "image/kulai10", "image/kulai11"]
image4 = Image.open(slidingimage[number - 1] + ".png")
st.image(image4.resize((1000, 500)))
st.header("  ")
st.header("  ")

numbe1r = st.slider("请滑动来观看更多资讯与照片 Pictures and Info, Please Slide to view", 1, 4, key="cremation")

slidingimage1 = ["image/kulai12", "image/kulai13", "image/kulai14", "image/kulai15"]
image2 = Image.open(slidingimage1[numbe1r - 1] + ".png")
st.image(image2.resize((1000, 500)))
