import streamlit as st
from PIL import Image
import imageslider


st.set_page_config(layout="wide")
st.header("Welcome to our Nirvana Funeral Parlour")
st.header(" 欢迎来到Nirvana富贵")
image1 = Image.open("image/kulai1.jpg")
st.image(image1.resize((1000, 600)))

content1 = """
✨✨✨✨✨事前规划，心无牵挂✨✨✨✨✨\n
✔根据自己的意愿规划，无需贷款 0% 利息供期✔\n
⭐⭐⭐⭐⭐全方位的一条龙服务⭐⭐⭐⭐⭐

我提供的服务包括：“骨灰福位、风水宝地、殡仪配套、遗嘱规划、神主牌位、龙龟生基"""
content2 = """
To prepare in advance for a peaceful mind
To plan according to your wants, with no liability
We even have 0% interest rate installment plans
Our services include Burial, Cremation, Ancestral Plate
and many more!"""

content5 = """
那什么是事前规划呢？\n
事前规划,是通过自身主权\n
在生前预先把身后事安排妥当\n

死亡是公平的,不会等待也无法避免,
因此事前规划,对每个人都很重要\n
\n
What is Pre-planning?\n
Pre-planning means advance planning of your final
send-off before the needs occurs.
Death does not discriminate, it’s doesn’t wait, and it is
inevitable.
This is exactly why pre-planning is important for
everyone.
"""
st.write(content5)
st.write(content1)
st.write(content2)


# imageslider.imageslider1()

number = st.slider("For more info", 0, 1)

slidingimage = ["image/image1", "image/image2"]
image2 = Image.open(slidingimage[number] + ".png")
st.image(image2.resize((1000, 500)))



content3 = """
想要了解我们的服务与产品，请看左边\n
To further understand our products, please take a look on the left"""
st.write(content3)

# Contact Me Send Email
st.header("Contact Me")
content4 = """
Whatsapp : +6010-3220722\n
Email : zhisean@gmail.com"""
st.write(content4)