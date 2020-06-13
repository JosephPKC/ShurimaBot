from abc import abstractmethod
from typing import Callable, Dict

from . import BaseAPI
from ..tools import Cache, Logger

class BaseRiotAPI(BaseAPI.BaseAPI):
    def __init__(self, cache: Cache.Cache, logger: Logger.Logger, timeout: int, riot_key: str) -> None:
        self._riot_key: str = riot_key

        self.timeout: int = timeout
        self._cache: Cache.Cache = cache
        self._logger: Logger.Logger = logger

        super().__init__(cache, logger, timeout, riot_key)

    def _get_extra_params(self) -> Dict:
        params: Dict = dict()

        # Add params here
        params['timeout'] = self.timeout

        return params

    def _get_headers(self) -> Dict:
        headers: Dict = dict()

        # Add headers here
        headers['X-Riot-Token'] = self._riot_key

        return headers

    def _get_riot_api_url(self, prefix: str, method_url: str) -> str:
        return f"https://{prefix}.api.riotgames.com/lol/{method_url}"

    @abstractmethod
    def _get_default_ttl(self) -> int:
        return 60 # Default 1 min