import os
import time

import smtplib
from dotenv import load_dotenv

from providers import PROVIDERS
from receivers import RECEIVERS


def send_message(sender_email, sender_password, receiver_address, receiver_name, sender_name):
    print(f"\nSending a message to: {receiver_address}")

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_email, sender_password)

    # message to be sent
    subject = "SMTP email test 2"
    message_content = "This is the test email's message."
    message = f"From: {sender_name} <{sender_email}>\n" \
              f"To: {receiver_name} <{receiver_address}>\n" \
              f"Subject: {subject}\n" \
              f"{message_content}"

    # sending the mail
    s.sendmail(sender_email, receiver_address, message)

    # terminating the session
    s.quit()

    print(f"Message successfully sent to: {receiver_address}")


if __name__ == "__main__":
    start_time = time.time()

    print("-------------Starting Email Program----------------")

    # load env variables
    load_dotenv()
    sender_email_id = os.getenv("SENDER_EMAIL_ID")
    sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")
    sender_name = os.getenv("SENDER_NAME")

    # gmail disabled insecure apps after May 2022, so now using an app password generated in gmail is a must
    sender_email_app_password = os.getenv("SENDER_EMAIL_APP_PASSWORD")

    for receiver in RECEIVERS.keys():
        receiver_address_id = receiver
        receiver_name = RECEIVERS[receiver]["name"]
        mms_support = False

        # if the receiver is a phone number
        if RECEIVERS[receiver]["phone"]:
            provider = RECEIVERS[receiver]["provider"]
            if PROVIDERS[provider]["mms_support"]:
                mms_support = True
                receiver_address_id = receiver + "@" + PROVIDERS[provider]["mms"]
            else:
                receiver_address_id = receiver + "@" + PROVIDERS[provider]["sms"]
        send_message(sender_email_id, sender_email_app_password, receiver_address_id, receiver_name, sender_name)

    print("-------------Ending Email Program----------------")
    print("--- %s seconds ---" % (time.time() - start_time))
