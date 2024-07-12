import streamlit as st
import send_email as seem
from email.mime.text import MIMEText
from PIL import Image
import imageslider


st.set_page_config(layout="wide")
st.header("Welcome to our Nirvana Funeral Parlour")
st.header(" 欢迎来到Nirvana富贵")
image1 = Image.open("image/kulai1.jpg")
st.image(image1.resize((1000, 600)))

content1 = """
✨事前规划，心无牵挂✨\n
根据自己的意愿规划，无需贷款 0% 利息供期✔\n
全方位的一条龙服务⭐⭐⭐⭐⭐

我提供的服务包括：“骨灰福位、风水宝地、殡仪配套、遗嘱规划、神主牌位、龙龟生基"""
content2 = """
To prepare in advance for a peaceful mind
To plan according to your wants, with no liability
We even have 0% interest rate installment plans
Our services include Burial, Cremation, Ancestral Plate
and many more!"""

st.write(content1)
st.write(content2)
image2 = Image.open("image/image1.png")
st.image(image2.resize((1000, 450)))
# imageslider.imageslider1()

image3 = Image.open("image/image2.png")
st.image(image3.resize((1000, 450)))

content3 = """
想要了解我们的服务与产品，请看左边\n
To further understand our products, please take a look on the left"""
st.write(content3)

# Contact Me Send Email
st.header("Contact Me")
content4 = """
Whatsapp : +6010-3220722"""
st.write(content4)

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        format_text = MIMEText(message, 'plain', 'utf-8')
        message2 = f"""\
        Subject: New email from {user_email}
        {user_email}\n
        {format_text} 
        """
        seem.send_email(message2)
        st.info("Your message is received. I will be replying soon.tm. XD")
