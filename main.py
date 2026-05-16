from scripts.extract import extract_weather
from scripts.transform import transform_weather
from scripts.load import load_to_postgres

def run_pipeline(cities):
    for city in cities:
        print(f"Processing: {city}")
        raw_data = extract_weather(city)
        clean_df = transform_weather(raw_data)
        load_to_postgres(clean_df)
        print(f"Done: {city}\n")

if __name__ == "__main__":
    cities = ["Mumbai", "Pune", "Nashik", "Bangalore"]
    run_pipeline(cities)