import pandas as pd
from datetime import datetime, timezone

def transform_weather(raw_data):
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
    return df

# Test block — only runs when you execute this file directly
if __name__ == "__main__":
    # Sample data copied from your actual API output above
    sample_raw = {
        "name": "Mumbai",
        "sys": {"country": "IN"},
        "main": {
            "temp": 31.99,
            "feels_like": 37.67,
            "humidity": 62
        },
        "weather": [{"description": "haze"}],
        "wind": {"speed": 3.6}
    }
    df = transform_weather(sample_raw)
    print(df)
    print("\nColumns:", df.columns.tolist())
    print("Shape:", df.shape)