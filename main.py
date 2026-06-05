import requests
from twilio.rest import Client
import os

account_sid=os.environ.get("SID_ACCOUNT")
api_key=os.environ.get("OWM_API_KEY")
auth_token=os.environ.get("AUTH_KEY")
from_number = os.environ.get("TWILIO_FROM")
to_number = os.environ.get("TWILIO_TO")

MY_LAT = 53.914730
MY_LONG = 15.198460



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters
)

print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for period in weather_data["list"]:
    if period["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔ ",
        from_=from_number,
        to=to_number,
    )
    print(message.status)
