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