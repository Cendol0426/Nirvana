import streamlit as st
import send_email as seem
from email.mime.text import MIMEText

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