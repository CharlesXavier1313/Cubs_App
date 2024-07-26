import requests
import pandas as pd
import logging
from time import sleep

# Configure logging
logging.basicConfig(filename='fetch_odds_data.log', level=logging.INFO)

# The Odds API endpoint for odds data
ODDS_API_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds"
API_KEY = "your_api_key_here"

def fetch_odds_data():
    retries = 5
    for i in range(retries):
        try:
            response = requests.get(ODDS_API_URL, params={"apiKey": API_KEY})
            response.raise_for_status()
            data = response.json()
            odds_data = pd.json_normalize(data)
            return odds_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching odds data: {e}")
            sleep(2 ** i)  # Exponential backoff
    return None

if __name__ == "__main__":
    odds_data = fetch_odds_data()
    if odds_data is not None:
        odds_data.to_csv('odds_data.csv', index=False)
        logging.info("Odds data fetched and saved successfully.")
