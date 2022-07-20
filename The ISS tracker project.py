import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.520430
MY_LONG = 73.856743

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
position_iss=[iss_longitude,iss_latitude]


#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    if 15 < iss_latitude < 23 or 67 < iss_longitude < 78 or sunset <= time_now.hour <= sunrise:
        my_email = "xabc31480@gmail.com"
        password = "bzbgtmnackvfwgkh"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:ISS incoming\n\nLook up")
        connection.close()










