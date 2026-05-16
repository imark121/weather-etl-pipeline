import requests
import os
from dotenv import load_dotenv
from config.logger import get_logger

load_dotenv()
logger = get_logger("extract")

def extract_weather(city="Mumbai"):
    logger.info(f"Starting extraction for city: {city}")
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": os.getenv("API_KEY"),
            "units": "metric"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        logger.info(f"Successfully extracted data for: {city}")
        return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f"No internet connection. Could not fetch data for: {city}")
        return None

    except requests.exceptions.Timeout:
        logger.error(f"API request timed out for: {city}")
        return None

    except requests.exceptions.HTTPError as e:
        logger.error(f"API returned an error for {city}: {e}")
        return None