import requests
import vonage
parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "daily,minutely,current",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
for item in range(0, 11):
    ide = int(data["hourly"][item]["weather"][0]["id"])
    if ide<700:
        client = vonage.Client(key="5f06ee65", secret="fT7lOhv3zQlJyKOp")
        sms = vonage.Sms(client)
        responseData = sms.send_message(
            {
                "from": "Vonage APIs",
                "to": +917709266305,
                "text": "It's going to rain please bring umbrella",
            }
        )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

        break
