import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
sender_email_id = os.getenv("SENDER_EMAIL_ID")
sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")
receiver_email_id = os.getenv("RECEIVER_EMAIL_ID")

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email_id, sender_email_password)

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail(sender_email_id, "receiver_email_id", message)

# terminating the session
s.quit()
