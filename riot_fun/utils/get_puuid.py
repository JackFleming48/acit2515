from dotenv import load_dotenv
from enum import Enum
import requests
import os


load_dotenv()

class Regions(Enum):
    # implement prompt and checking
    #  prompt == Regions.{prompt}.name.lower()
    # use that in api string...
    americas = 1
    asia = 2
    europe = 3

class GetPuuid:
    
    def __init__(self, summoner_name: str, tagline: str):
        '''
        Region codes: americas, asia, europe
        '''
        self._api_key = os.getenv("RIOT_KEY")
        self.summoner_name = summoner_name
        self.tagline = tagline

    @property
    def get_summoner_info(self):
        headers = {
            'X-Riot-Token': self._api_key
        }
        url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{self.summoner_name}/{self.tagline}"

        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred getting summoner name: {e}")

