import csv
import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header

from collections import namedtuple

# replace with real password
password = '42'

Promo = namedtuple("Promo", "first_name email discount_code")

email_template = """
Hi {first_name},
last weekend was like a roller coaster ride! We've forgot to give you a nice
gift from our silver sponsor PyCharm - the discount code for personal licenses.

Here it is:

{discount_code}

The code gives you 20% discount from PyCharm personal license subscription,
new or renewal. It's valid until 14th December 2015.

You can buy or renew PyCharm here: https://www.jetbrains.com/pycharm/buy/#personal

If you still have some questions, contact PyCharm support at promo@jetbrains.com.


Cheers,
   PyCon CZ team


Note: More info about PyCon CZ 2015 (photos, videos, report) coming soon.
"""

test_recipient = Promo("Tomas", "tomas.ehrlich@gmail.com", "ABCD-EFGH-IJKL")


def send_email(recipient, smtp):
    body = email_template.format(
        first_name=recipient.first_name.capitalize(),
        discount_code=recipient.discount_code
    )
    msg = MIMEText(body)
    msg['Subject'] = 'PyCharm discount code'
    msg['From'] = 'info@pycon.cz'
    msg['To'] = recipient.email
    return smtp.send_message(msg)


def send_bulk_email(smtp):
    with open('jetbrains-codes.csv', newline='') as io:
        recipients = csv.reader(io, delimiter=',')
        for data in recipients:
            recipient = Promo(*data)
            print("Sending to {email}".format(email=recipient.email))
            send_email(recipient, smtp)
            time.sleep(1)


smtp = smtplib.SMTP_SSL('smtp.zoho.com')
smtp.login('info@pycon.cz', password)

send_email(test_recipient, smtp)
yes = input("Testing email send. Check it. Do you want to send 250 emails now? [y/N]")

if yes == "y":
    send_bulk_email(smtp)

smtp.quit()
