import os
import smtplib
from dotenv import load_dotenv

from providers import PROVIDERS
from receivers import RECEIVERS


def send_message(sender_email, sender_password, receiver_address):
    print(f"Sending a message to: {receiver_address}")

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_email, sender_password)

    # message to be sent
    message = "Hello World"

    # sending the mail
    s.sendmail(sender_email, receiver_address, message)

    # terminating the session
    s.quit()

    print(f"Message successfully sent to: {receiver_address}")


if __name__ == "__main__":
    print("running main")
    # load env variables
    load_dotenv()
    sender_email_id = os.getenv("SENDER_EMAIL_ID")
    sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")

    # gmail disabled insecure apps after May 2022, so now using an app password generated in gmail is a must
    sender_email_app_password = os.getenv("SENDER_EMAIL_APP_PASSWORD")
    # receiver_email_id = os.getenv("RECEIVER_EMAIL_ID")

    for receiver in RECEIVERS.keys():
        receiver_address_id = receiver
        mms_support = False

        # if the receiver is a phone number
        if RECEIVERS[receiver]["phone"]:
            provider = RECEIVERS[receiver]["provider"]
            if PROVIDERS[provider]["mms_support"]:
                mms_support = True
                receiver_address_id = receiver + "@" + PROVIDERS[provider]["mms"]
            else:
                receiver_address_id = receiver + "@" + PROVIDERS[provider]["sms"]
        send_message(sender_email_id, sender_email_app_password, receiver_address_id)
