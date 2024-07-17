import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("龙龟生机 NV Seed")
image1 = Image.open("image/kulai27.png")
st.image(image1.resize((1000, 500)))
st.write("""生基也称寿坟、寿穴、是活人的生坟。
生基,即是“生命的根基”,生基风水借助
大自然的磁场力量,强化个人八字根基的弱
点,融合阴宅与阳宅之间的风水秘法,为福
主添福添寿,提升运势及转运。""")

st.write("""Sheng Ji means ‘the foundation of life’. Sheng Ji plays a key role in
strengthening the foundation of your destiny by harnessing the good
“Qi” from the environment, helps correct the weakness of Bazi.
Sheng Ji is a complex workaround between a human dwelling and a
tomb.Sheng Ji able to enhance one’s luck and course of destiny.""")

image = Image.open("image2/nvseed1.png")
st.image(image.resize((1000, 500)))
