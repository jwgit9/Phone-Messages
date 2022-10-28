import os
import time

import smtplib
from dotenv import load_dotenv

from providers import PROVIDERS
from receivers import RECEIVERS


def send_message(receiver_email, receiver_name, subject, message):
    print(f"\nSending a message to: {receiver_email}")

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_username, sender_password)

    # message to be sent
    formatted_message = f"From: {sender_name} <{sender_username}>\n" \
                        f"To: {receiver_name} <{receiver_email}>\n" \
                        f"Subject: {subject}\n" \
                        f"{message}"

    # sending the mail
    s.sendmail(sender_username, receiver_email, formatted_message)

    # terminating the session
    s.quit()

    print(f"Message successfully sent to: {receiver_email}")


# Finds the email address to send for a receiver
def find_receiver_info(receiver_id):
    receiver_email = receiver_id
    receiver_name = RECEIVERS[receiver]["name"]
    mms_support = False

    # if the receiver is a phone number
    if RECEIVERS[receiver]["phone"]:
        provider = RECEIVERS[receiver]["provider"]
        if PROVIDERS[provider]["mms_support"]:
            mms_support = True
            receiver_email = receiver + "@" + PROVIDERS[provider]["mms"]
        else:
            receiver_email = receiver + "@" + PROVIDERS[provider]["sms"]

    return [receiver_email, receiver_name]


if __name__ == "__main__":
    start_time = time.time()
    print("-------------Starting Email Program----------------")

    # load env variables
    load_dotenv()
    sender_name = os.getenv("SENDER_NAME")
    sender_username = os.getenv("SENDER_EMAIL_ID")

    # gmail disabled insecure apps after May 2022, so now using an app password generated in gmail is a must
    sender_password = os.getenv("SENDER_EMAIL_APP_PASSWORD")

    for receiver in RECEIVERS.keys():
        receiver_info = find_receiver_info(receiver)
        update_subject = "SMTP Email Test 3"
        update_message = "This is the test email's message."
        send_message(receiver_info[0], receiver_info[1], update_subject, update_message)

    print("-------------Ending Email Program----------------")
    print("--- %s seconds ---" % (time.time() - start_time))
