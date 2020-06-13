from typing import Callable

from . import BaseRiotAPI
from ..data import Summoner
from ..tools import Cache, Enums

class SummonerAPI(BaseRiotAPI.BaseRiotAPI):
    def __init__(self, cache: Cache.Cache, timeout: int, riot_key: str) -> None:
        super().__init__(cache, timeout, riot_key)

    def by_name(self, summoner_name: str, region: Enums.LOLRegion, ttl: int = None) -> object:
        method: str = f"summoner/v4/summoners/by-name/{summoner_name}"
        return self.__retrieve_summoner_data(method, region, ttl)

    def by_account_id(self, account_id: str, region: Enums.LOLRegion, ttl: int = None) -> object:
        method: str = f"summoner/v4/summoners/by-account/{account_id}"
        return self.__retrieve_summoner_data(method, region, ttl)

    def __retrieve_summoner_data(self, method: str, region: Enums.LOLRegion, ttl: int) -> object:
        url: str = super()._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Summoner.Summoner(r)

        return super().retrieve_data(url, builder, ttl=ttl)
    
    def _get_default_ttl(self) -> int:
        return 600 # Default to 10 minutes