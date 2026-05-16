from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df):
    engine = create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    df.to_sql(
        name="weather_data",
        con=engine,
        if_exists="append",
        index=False
    )
    print(f"Successfully loaded {len(df)} row(s) into weather_data table.")

if __name__ == "__main__":
    import pandas as pd
    from datetime import datetime

    sample_df = pd.DataFrame([{
        "city":         "Mumbai",
        "country":      "IN",
        "temperature":  31.99,
        "feels_like":   37.67,
        "humidity":     62,
        "weather_desc": "haze",
        "wind_speed":   3.6,
        "extracted_at": datetime.now()
    }])
    load_to_postgres(sample_df)