import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",
    "lang": "uk"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
else:
    print("Error getting weather data. Please check the city name.")
    print("Details:", response.json())
