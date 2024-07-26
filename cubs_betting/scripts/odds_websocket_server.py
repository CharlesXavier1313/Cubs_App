import asyncio
import websockets
import json
import random
import logging

# Configure logging
logging.basicConfig(filename='odds_websocket_server.log', level=logging.INFO)

async def odds_update(websocket, path):
    while True:
        odds_update = {
            "game_id": random.randint(1, 100),
            "bookmaker": random.choice(["DraftKings", "FanDuel", "BetMGM"]),
            "odds_type": random.choice(["moneyline", "spread", "total"]),
            "odds_value": round(random.uniform(1.5, 3.0), 2)
        }
        await websocket.send(json.dumps(odds_update))
        logging.info(f"Sent odds update: {odds_update}")
        await asyncio.sleep(5)  # Simulate real-time updates every 5 seconds

start_server = websockets.serve(odds_update, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
