from scripts.extract import extract_weather
from scripts.transform import transform_weather
from scripts.load import load_to_postgres
from config.logger import get_logger

logger = get_logger("main")

def run_pipeline(cities):
    logger.info("=" * 50)
    logger.info("Pipeline started")
    logger.info("=" * 50)

    success = 0
    failed  = 0

    for city in cities:
        logger.info(f"Processing city: {city}")
        raw_data = extract_weather(city)
        clean_df = transform_weather(raw_data)
        load_to_postgres(clean_df)

        if clean_df is not None:
            success += 1
        else:
            failed += 1

    logger.info("=" * 50)
    logger.info(f"Pipeline finished — Success: {success} | Failed: {failed}")
    logger.info("=" * 50)

if __name__ == "__main__":
    cities = ["Mumbai", "FakeCity123", "Nashik", "Bangalore"]
    run_pipeline(cities)