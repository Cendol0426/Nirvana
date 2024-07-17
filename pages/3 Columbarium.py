import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("骨灰殿, Columbarium")
image7 = Image.open("image/image7.png")
st.image(image7.resize((720, 360)))
image9 = Image.open("image/image9.png")
st.image(image9.resize((720, 360)))
content = """
以上资料是关于骨灰位与辈分的关系\n
Above is information about the relation between seats and elderly"""
st.info(content)
image1 = Image.open("image/kulai28.png")
st.image(image1.resize((720, 360)))