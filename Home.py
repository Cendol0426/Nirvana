import streamlit as st
import send_email as seem
from email.mime.text import MIMEText
from PIL import Image
import imageslider


st.set_page_config(layout="wide")
st.header("Welcome to our Nirvana， 欢迎来到Nirvana富贵")
image1 = Image.open("image/kulai1.jpg")
st.image(image1.resize((1000, 600)))

content1 = """
✨事前规划，心无牵挂✨\n
根据自己的意愿规划，无需贷款 0% 利息供期✔\n
全方位的一条龙服务⭐⭐⭐⭐⭐

我提供的服务包括：“骨灰福位、风水宝地、殡仪配套、遗嘱规划、神主牌位、龙龟生基"""

st.write(content1)
image2 = Image.open("image/image1.png")
st.image(image2.resize((1000, 450)))
# imageslider.imageslider1()

image3 = Image.open("image/image2.png")
st.image(image3.resize((1000, 450)))

col1, emptycol1, col2 = st.columns((2, 0.5, 2))
with col1:
    image3 = Image.open("image/image3.png")
    st.image(image3.resize((720, 360)))
    image4 = Image.open("image/image4.png")
    st.image(image4.resize((720, 360)))
    image5 = Image.open("image/image5.png")
    st.image(image5.resize((720, 360)))
    image6 = Image.open("image/image6.png")
    st.image(image6.resize((720, 360)))

with col2:
    image7 = Image.open("image/image7.png")
    st.image(image7.resize((720, 360)))
    image8 = Image.open("image/image8.png")
    st.image(image8.resize((720, 360)))
    image9 = Image.open("image/image9.png")
    st.image(image9.resize((720, 360)))


# Contact Me Send Email
st.header("Contact Me")

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
