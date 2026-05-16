# Weather ETL Pipeline

An end-to-end ETL pipeline that extracts live weather data from the OpenWeatherMap API, transforms it into a structured format, and loads it into a PostgreSQL database.

## Tech Stack
- **Python** — core pipeline logic
- **Pandas** — data transformation
- **PostgreSQL** — data storage
- **SQLAlchemy** — database connection
- **Apache Airflow** — pipeline scheduling (coming soon)

## Pipeline Architecture
OpenWeatherMap API → extract.py → transform.py → load.py → PostgreSQL

## Project Structure
weather-etl-pipeline/
├── scripts/
│   ├── extract.py       # Calls weather API, returns raw JSON
│   ├── transform.py     # Cleans and structures raw data
│   └── load.py          # Loads data into PostgreSQL
├── dags/
│   └── weather_etl_dag.py  # Airflow DAG (coming soon)
├── config/
│   └── config.py        # Configuration settings
├── main.py              # Pipeline entry point
├── requirements.txt     # Python dependencies
└── .env                 # API keys and DB credentials (not committed)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/imark121/weather-etl-pipeline.git
cd weather-etl-pipeline
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
API_KEY=your_openweathermap_api_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_project
DB_USER=your_postgres_username
DB_PASS=your_postgres_password

### 5. Set up PostgreSQL
Create the database and table:
```sql
CREATE DATABASE etl_project;

CREATE TABLE weather_data (
    id            SERIAL PRIMARY KEY,
    city          VARCHAR(100),
    country       VARCHAR(10),
    temperature   FLOAT,
    feels_like    FLOAT,
    humidity      INT,
    weather_desc  VARCHAR(200),
    wind_speed    FLOAT,
    extracted_at  TIMESTAMP
);
```

### 6. Run the pipeline
```bash
python3 main.py
```

## Sample Output
| city | country | temperature | feels_like | humidity | weather_desc | wind_speed | extracted_at |
|------|---------|-------------|------------|----------|--------------|------------|--------------|
| Mumbai | IN | 31.99 | 37.67 | 62 | haze | 3.6 | 2026-05-16 04:26:58 |
| Pune | IN | 29.50 | 33.20 | 58 | clear sky | 2.1 | 2026-05-16 04:27:01 |

## What I Learned
- Building an end-to-end ETL pipeline from scratch
- Consuming REST APIs and handling JSON responses
- Data transformation using Pandas
- Loading data into PostgreSQL using SQLAlchemy
- Managing credentials securely using environment variables
- Python project structure and separation of concerns

## Upcoming Improvements
- Add Apache Airflow for scheduling
- Add logging and error handling
- Add data quality checks
- Push to cloud (AWS S3 + Redshift)