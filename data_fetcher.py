import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FPLDataFetcher:
    BASE_URL = "https://fantasy.premierleague.com/api"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_bootstrap_data(self):
        url = f"{self.BASE_URL}/bootstrap-static/"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            players = pd.DataFrame(data['elements'])
            teams = pd.DataFrame(data['teams'])
            gameweeks = pd.DataFrame(data['events'])
            
            logger.info(f"Fetched {len(players)} players")
            
            return {
                'players': players,
                'teams': teams,
                'gameweeks': gameweeks
            }
            
        except Exception as e:
            logger.error(f"Error: {e}")
            return None
    
    def fetch_player_history(self, player_id):
        url = f"{self.BASE_URL}/element-summary/{player_id}/"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                'history': pd.DataFrame(data['history']),
                'fixtures': pd.DataFrame(data['fixtures'])
            }
        except Exception as e:
            logger.error(f"Error fetching player {player_id}: {e}")
            return None