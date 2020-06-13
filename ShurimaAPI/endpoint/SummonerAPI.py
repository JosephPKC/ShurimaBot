from typing import Callable

from . import BaseAPI
from ..data import Summoner
from ..tools import Cache, Enums, Logger

class SummonerAPI(BaseAPI.BaseAPI):

    _ttl: int = 600 # Summoner information stays for 10 minutes

    def __init__(self, cache: Cache.Cache, logger: Logger.Logger, timeout: int, riot_key: str) -> None:
        super().__init__(cache, logger, timeout, riot_key)

    def by_name(self, summoner_name: str, region: Enums.LOLRegion) -> object:
        method: str = f"summoner/v4/summoners/by-name/{summoner_name}"
        url: str = super()._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Summoner.Summoner(r)

        return super().retrieve_data(url, self._ttl, builder)