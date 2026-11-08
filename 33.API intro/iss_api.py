import requests
import datetime as dt
import smtplib
import time


MY_EMAIL = "fortressking67890@gmail.com"
my_password = "unct amgg zfdw lnsu"

parameters = {
    "lat" : 49.841525,
    "lng" : 8.175675,
    "formatted" : 0,
}
# sending mail once the iss is near me and its datk outside
def send_mail():
    with smtplib.SMTP("smtp.gmal.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password= my_password)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= "shreya69122@gmail.com",
                            msg= "Subject: ISS is ner your location \n\n ISS is currently avaialbe for lookup"
                            )
        
# Iss api endpoint
def check_iss():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    int_latitude = round(float(latitude),1)
    int_longitude = round(float(longitude),1)
    int_lat = round(parameters['lat'],1)
    int_lng = round(parameters['lng'],1)

    if int_lat - 5 <= int_latitude <= int_lat + 5 and int_lng <= int_longitude <= int_lng + 5:
        return True

# Sunrise-sunset endpoint
def check_dark():
    current_time = dt.datetime.now(dt.timezone.utc) #Check current time 
    response = requests.get("https://api.sunrise-sunset.org/json",params=  parameters) #we can add params
    response.raise_for_status()

    sunset = response.json()['results']['sunset'].split("T")[1].split(":")[0]
    sunrise = response.json()['results']['sunrise'].split("T")[1].split(":")[0]

    if current_time.hour <= int(sunrise) or current_time.hour >= int(sunset):
        return True

while True:
    if check_dark() and check_iss():
        send_mail()
    elif not check_dark:
        print("Its not dark yet.")
    elif not check_iss():
        print("ISS is not overhead")

    time.sleep(60)
