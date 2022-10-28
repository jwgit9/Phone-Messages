import os
import smtplib
from dotenv import load_dotenv


def send_message(sender_email, sender_password, receiver_email):
    print("sending a message")
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_email, sender_password)

    # message to be sent
    message = "Hello World"

    # sending the mail
    s.sendmail(sender_email, receiver_email, message)

    # terminating the session
    s.quit()


if __name__ == "__main__":
    print("running main")
    # load env variables
    load_dotenv()
    sender_email_id = os.getenv("SENDER_EMAIL_ID")
    sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")

    # gmail disabled insecure apps after May 2022, so now using an app password generated in gmail is a must
    sender_email_app_password = os.getenv("SENDER_EMAIL_APP_PASSWORD")
    receiver_email_id = os.getenv("RECEIVER_EMAIL_ID")

    send_message(sender_email_id, sender_email_app_password, receiver_email_id)
