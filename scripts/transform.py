import pandas as pd
from datetime import datetime, timezone
from config.logger import get_logger

logger = get_logger("transform")

def transform_weather(raw_data):
    if raw_data is None:
        logger.warning("Received None from extract — skipping transformation")
        return None

    try:
        logger.info(f"Transforming data for city: {raw_data.get('name')}")
        record = {
            "city":         raw_data["name"],
            "country":      raw_data["sys"]["country"],
            "temperature":  raw_data["main"]["temp"],
            "feels_like":   raw_data["main"]["feels_like"],
            "humidity":     raw_data["main"]["humidity"],
            "weather_desc": raw_data["weather"][0]["description"],
            "wind_speed":   raw_data["wind"]["speed"],
            "extracted_at": datetime.now(timezone.utc)
        }
        df = pd.DataFrame([record])
        logger.info(f"Transformation successful — {len(df)} row(s) ready")
        return df

    except KeyError as e:
        logger.error(f"Missing expected field in API response: {e}")
        return None

    except Exception as e:
        logger.error(f"Unexpected error during transformation: {e}")
        return None