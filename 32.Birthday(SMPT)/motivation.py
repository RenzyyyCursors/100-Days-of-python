import smtplib
import datetime as dt
import random

MY_EMAIL = "fortressking67890@gmail.com"
password = "unct amgg zfdw lnsu"
today = dt.datetime.now()
day = today.weekday()

def send_email():
    with open("quotes.txt",'r') as file:
        list = file.readlines()
        quote = random.choice(list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=password)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="shreya69122@gmail.com",
                            msg=f"Subject:Thursday Quote \n\n {quote} "
        )

if day == 3:
    send_email()
