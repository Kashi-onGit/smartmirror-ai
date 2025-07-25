import requests
import geocoder
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather():
    g = geocoder.ip('me')
    city_name = g.city or "Delhi"

    API_key = os.getenv("OPENWEATHER_API_KEY")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = round(data['main']['temp'])
        temp_feel_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        return f"{city_name}: {weather_desc}, {temp}°C, Humidity: {humidity}%, Feel Like: {temp_feel_like}°C"
    else:
        return "Weather data not available"
