import requests
import pandas as pd
import logging
from time import sleep

# Configure logging
logging.basicConfig(filename='fetch_game_stats.log', level=logging.INFO)

# MLB Stats API endpoint for game stats
GAME_STATS_URL = "https://statsapi.mlb.com/api/v1/schedule"

def fetch_game_stats():
    retries = 5
    for i in range(retries):
        try:
            response = requests.get(GAME_STATS_URL)
            response.raise_for_status()
            data = response.json()
            game_stats = pd.json_normalize(data['dates'])
            return game_stats
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching game stats: {e}")
            sleep(2 ** i)  # Exponential backoff
    return None

if __name__ == "__main__":
    game_stats = fetch_game_stats()
    if game_stats is not None:
        game_stats.to_csv('game_stats.csv', index=False)
        logging.info("Game stats fetched and saved successfully.")

