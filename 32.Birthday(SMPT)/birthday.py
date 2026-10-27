import random
import datetime as dt
import pandas
import smtplib

MY_EMAIL = "fortressking67890@gmail.com"
MY_PASSWORD = "env"

def send_mail(name,email,year):
    random_to_3 = random.choice([1,2,3])
    with open(f"letter_templates/letter_{random_to_3}.txt",'r') as file:
        letter = file.read()
        replaced_letter = letter.replace("[NAME]",f"{name}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy {wish_year-year}th Birthday {name} \n\n{replaced_letter}"
        )

date_time = dt.datetime.now()
wish_year = date_time.year
wish_month = date_time.month
wish_day = date_time.day

data_import = pandas.read_csv("birthdays.csv")
data = pandas.DataFrame(data_import)
data_list = data.to_dict(orient='records')

for i in data_list:
    if i['month'] == wish_month and i['day'] == wish_day:
        sender_name = i["name"]
        sender_email = i["email"]
        sender_year = i["year"]
        send_mail(sender_name,sender_email,sender_year)









