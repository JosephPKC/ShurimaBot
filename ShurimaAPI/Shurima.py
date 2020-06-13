from typing import Callable, Dict

import requests

from .tools import Cache
from .endpoint import SummonerAPI

class Shurima:
    """
    Public interface to which the user can access the API endpoints.
    """

    # Add more optional args as more APIs are integratted
    def __init__(self, timeout: int, riot_key: str) -> None:
        self.timeout: int = timeout
        self._riot_key: str = riot_key

        # Initialize subprocesses
        self._cache: Cache.Cache = Cache.Cache()

        # Endpoints
        self.Summoner: SummonerAPI.SummonerAPI = SummonerAPI.SummonerAPI(self._cache, self.timeout, self._riot_key)

    @property
    def riot_key(self) -> str:
        return self._riot_key