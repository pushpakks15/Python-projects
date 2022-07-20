import requests
from datetime import datetime

APP_ID="9ad60846"
API_KEY="9f3fe8eb4f9c116911dab2cf29d74a0f"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": "85",
    "height_cm": "186",
    "age": "20"
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_parameters={
            "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": result["exercises"][0]["name"],
            "duration": result["exercises"][0]["duration_min"],
            "calories": result["exercises"][0]["nf_calories"]
        }
}
res=requests.post("https://api.sheety.co/66e24fa3b004145e255e91f3343ee288/myWorkouts/workouts",json=sheet_parameters)
print(res.text)
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('pushpakks15', '22495717')
header={"Authorization": "Basic cHVzaHBha2tzMTU6MjI0OTU3MTc="}
requests.get('https://httpbin.org/basic-auth/user/pass', auth="basic cHVzaHBha2tzMTU6MjI0OTU3MTc=")

