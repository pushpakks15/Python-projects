import requests
import datetime
# response=requests.get("http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data=response.json()
# print(data)
#
# latitude=data["iss_position"]["latitude"]
# longitude=data["iss_position"]["longitude"]
# print((latitude,longitude))

parameters={
    "lat":18.520430,
    "lng":73.856743,
    "formatted":0,
}
response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
now=datetime.datetime.now()
print(now.hour)
