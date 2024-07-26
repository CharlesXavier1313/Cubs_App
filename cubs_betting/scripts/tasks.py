from celery import Celery
import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='celery_tasks.log', level=logging.INFO)

app = Celery('tasks', broker='redis://localhost:6379/0')

ODDS_API_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds"
API_KEY = "your_api_key_here"

@app.task
def fetch_odds_data():
    try:
        response = requests.get(ODDS_API_URL, params={"apiKey": API_KEY})
        response.raise_for_status()
        data = response.json()
        odds_data = pd.json_normalize(data)
        odds_data.to_csv('odds_data.csv', index=False)
        logging.info("Odds data fetched and saved successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching odds data: {e}")
