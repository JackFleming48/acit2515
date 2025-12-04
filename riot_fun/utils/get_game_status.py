from dotenv import load_dotenv
from get_puuid import GetPuuid
import requests
import os

class GetGame:

    def __init__(self, puuid: str, tagline: str):
        self.puuid = puuid
        self.tagline = tagline
        self._api_key = os.getenv("RIOT_KEY")

    
    def url(self):
        return f"https://na1.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{self.puuid}"

    @property
    def get_summoner_game(self):
        headers = {
            'X-Riot-Token': self._api_key
        }
        url = self.url()

        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occured getting summoner game: {e}")


# iscoothd = GetPuuid("SHAYANT", "na1")
# iscoothd_game = GetGame(iscoothd.get_summoner_info["puuid"], iscoothd.get_summoner_info["tagLine"].lower())
# print(iscoothd_game.get_summoner_game["gameLength"])