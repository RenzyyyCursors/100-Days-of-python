# import smtplib

# my_email = "fortressking67890@gmail.com"
# password = "unct amgg zfdw lnsu"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="shreya69122@gmail.com",
#                         msg="Subject:Hello \n\n This is Body "
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(day,month)

date_of_biirth = dt.datetime(year = 2000,month=11,day=30)
print(date_of_biirth)

