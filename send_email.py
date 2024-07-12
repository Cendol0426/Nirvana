import smtplib, ssl
import os

def send_email(sendercontext):
    host = "smtp.gmail.com"
    port = 465

    username = "zhisean@gmail.com"
    password = os.getenv("PASSWORDFORGMAIL")

    receiver = "zhisean@gmail.com"
    mycontext = ssl.create_default_context()

    message = f"{sendercontext}"

    with smtplib.SMTP_SSL(host, port, context=mycontext) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address， 您的电邮地址，没有请放 - ")
    message = st.text_area("Your message, 想告诉我什么？")
    button = st.form_submit_button()
    if button:
        # format_text = MIMEText(message, 'plain', 'utf-8')
        message2 = f"""\
        Subject: New email from {user_email}
        New Email from {user_email}\n
        {message} 
        """
        seem.send_email(message2)
        st.info("Your message is received. I will be replying soon.tm. XD")
