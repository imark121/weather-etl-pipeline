import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_weather(city="Mumbai"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("API_KEY"),
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = extract_weather("Mumbai")
    print(data)