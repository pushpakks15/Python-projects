STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_FOR_NEWS="031e1fd3e7474d3ab65009c12e7faad1"
import requests
import datetime
import vonage
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":"TD6H16H9CUXAG058",
}
parameters_for_news={
    "apiKey":API_FOR_NEWS,
    "country":"us",
    "category":"business",

}

response=requests.get("https://www.alphavantage.co/query",params=parameters)
response.raise_for_status()
data=response.json()
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
yes_date=str(yesterday.date())
day_before_yesterday = datetime.datetime.now() - datetime.timedelta(days = 2)
day_before_date=str(day_before_yesterday.date())
yes=float(data["Time Series (Daily)"][yes_date]["4. close"])
day_before_yes=float(data["Time Series (Daily)"][day_before_date]["4. close"])
up_down=None
if yes>day_before_yes:
    diff=float(yes-day_before_yes)
    x=round((diff/day_before_yes)*100)
    up_down=f"🔺{x}%"
if yes<day_before_yes:
    diff=float(day_before_yes-yes)
    y=round((diff/day_before_yes)*100)
    up_down=f"🔻{y}%"

response_for_news=requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yes_date}&sortBy=popularity&apiKey={API_FOR_NEWS}")
response_for_news.raise_for_status()
news=response_for_news.json()
for n in range(3):
    headline=news["articles"][n]["title"]
    brief=news["articles"][n]["description"]

client = vonage.Client(key="5f06ee65", secret="fT7lOhv3zQlJyKOp")
sms = vonage.Sms(client)
responseData = sms.send_message(
{
                "from": "Vonage APIs",
                "to": +917709266305,
                "text": f"{up_down}\nHeadline:{headline}\nBrief:{brief}",
}
)

if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")








