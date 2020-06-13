import requests

from abc import ABC
from typing import Callable, Dict

from ..tools import Cache, Logger

class BaseAPI(ABC):
    def __init__(self, cache: Cache.Cache, logger: Logger.Logger, timeout: int, riot_key: str) -> None:
        self._riot_key: str = riot_key

        self.timeout: int = timeout
        self._cache: Cache.Cache = cache
        self._logger: Logger.Logger = logger

        super().__init__()

    def retrieve_data(self, url: str, ttl: int, builder: Callable, params: Dict = None) -> object:
        """
        Helper function that will attempt to retrieve information.
        """

        # Check cache first.
        request_url: str = requests.Request("GET", url, params=params).prepare().url
        result: object = self._cache.search(request_url)

        if result is not None:
            return result

        # Try sending a request if not found.
        try:
            response: requests.Response = self._send_request(url, params)
            result = builder(response.json())
            self._cache.add(url, result, ttl)
            return result
        except Exception as e:
            self._logger.log(e)
            raise e # Raise the exception to let caller know.

    def _send_request(self, url: str, params: Dict = None) -> requests.Response:
        if params is not None:
            # Clean up the params, and remove any empty values.
            params: Dict = {k: v for k, v in params.items() if v is not None}

        extra_params: Dict = self.__get_riot_api_params()
        headers: Dict = self.__get_riot_api_headers()
        response: requests.Response = requests.get(url, params, headers=headers, **extra_params)

        # 200 - OK
        if response.status_code != 200:
            raise Exception(response.status_code)

        return response

    #region API specific params and headers
    def __get_riot_api_params(self) -> Dict:
        params: Dict = dict()

        # Add params here
        if self.timeout is not None:
            params['timeout'] = self.timeout

        return params

    def __get_riot_api_headers(self) -> Dict:
        headers: Dict = dict()

        # Add headers here
        headers['X-Riot-Token'] = self._riot_key

        return headers

    def _get_riot_api_url(self, prefix: str, method_url: str) -> str:
        return f"https://{prefix}.api.riotgames.com/lol/{method_url}"
    #endregion