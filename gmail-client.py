import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hello there")

msg["Subject"] = f"This is subject"
msg["From"] = "bella.belgarokova@hotmail.com"
msg["To"] =  "bella.belgarokova@hotmail.com"

s = smtplib.SMTP("127.0.0.1")
s.send_message(msg)
s.quit()