import requests
import pandas as pd
import logging
from time import sleep

# Configure logging
logging.basicConfig(filename='fetch_player_stats.log', level=logging.INFO)

# MLB Stats API endpoint for player stats
PLAYER_STATS_URL = "https://statsapi.mlb.com/api/v1/stats"

def fetch_player_stats():
    retries = 5
    for i in range(retries):
        try:
            response = requests.get(PLAYER_STATS_URL)
            response.raise_for_status()
            data = response.json()
            player_stats = pd.json_normalize(data['stats'])
            return player_stats
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching player stats: {e}")
            sleep(2 ** i)  # Exponential backoff
    return None

if __name__ == "__main__":
    player_stats = fetch_player_stats()
    if player_stats is not None:
        player_stats.to_csv('player_stats.csv', index=False)
        logging.info("Player stats fetched and saved successfully.")

