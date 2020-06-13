from abc import abstractmethod
from typing import Callable, Dict

from . import BaseAPI
from ..tools import Cache

class BaseRiotAPI(BaseAPI.BaseAPI):
    def __init__(self, cache: Cache.Cache, timeout: int, riot_key: str) -> None:
        super().__init__(cache, timeout, riot_key)

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
        return None