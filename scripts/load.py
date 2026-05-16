from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from config.logger import get_logger

load_dotenv()
logger = get_logger("load")

def load_to_postgres(df):
    if df is None:
        logger.warning("Received None from transform — skipping load")
        return

    try:
        logger.info(f"Loading {len(df)} row(s) into PostgreSQL")
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
        logger.info("Load successful")

    except Exception as e:
        logger.error(f"Failed to load data into PostgreSQL: {e}")