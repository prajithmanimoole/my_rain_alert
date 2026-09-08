import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
weather_api = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
"lat" : 12.7445,
"lon" : 75.0288,
"appid" : weather_api,
"cnt" : 4,
}

url = OWM_Endpoint
response = requests.post(url,params=parameters)
response.raise_for_status()
weather_data = response.json()

# list_of_weather_id = [weather_data["list"][i]["weather"][0]["id"] for i in range(len(weather_data["list"]))]
list_of_weather_id = [hour_data["weather"][0]["id"] for hour_data in (weather_data["list"])]
print(list_of_weather_id)
will_rain = False
if any(list_of_weather_id) < 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+918088016312",
        from_="+17372212163",
        body="sms_event_notifications",
    )

    msg = client.messages.create(
        to="whatsapp:+918088016312",
        from_="whatsapp:+17372212163",
        content_sid="HXd3d932e8cb4598189831c97250c43d17",
    )
    print(msg.status)
    print(message.status)
