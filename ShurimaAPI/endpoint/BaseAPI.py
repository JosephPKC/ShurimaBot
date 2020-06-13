import requests

from abc import ABC, abstractmethod
from typing import Callable, Dict

from .. import config
from ..tools import Cache, Misc

class BaseAPI(ABC):
    """ BaseAPI is the base class for all API endpoints.
    """
    def __init__(self, cache: Cache.Cache, timeout: int, riot_key: str) -> None:
        """ Constructor for abstract BaseAPI.

        Args:
            cache (Cache.Cache): The cache manager.
            timeout (int): The amount of seconds to wait after sending a request before timing out.
            riot_key (str): The API key for riot's API.
        """
        self._riot_key: str = riot_key

        self.timeout: int = timeout
        self._cache: Cache.Cache = cache

        super().__init__()
    
    @Misc.timer(config.DEBUG)
    def retrieve_data(self, url: str, builder: Callable, ttl: int = None, params: Dict = None) -> object:
        """ Retrieves data based on url. It will check the cache first. Otherwise, it will attempt an API call.

        Args:
            url (str): The url for the API endpoint. This also acts as the key for the cache.
            builder (Callable): The build function for the data container. This will determine how we build the resulting data container.
            ttl (int, optional): [description]. The time to live for the data when caching. Defaults to None.
            params (Dict, optional): [description]. The parameters for the API request. Defaults to None.

        Raises:
            e: General exception that can occur when retrieving from the API endpoint.

        Returns:
            object: The resulting data container that contains all of the info from the API endpoint or cache.
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

            if ttl is None:
                ttl = self._get_default_ttl()

            self._cache.add(url, result, ttl)
            return result
        except Exception as e:
            print(e) # Just print for now
            raise e # Raise the exception to let caller know.

    @Misc.timer(config.DEBUG)
    
    def _send_request(self, url: str, params: Dict = None) -> requests.Response:
        if params is not None:
            # Clean up the params, and remove any empty values.
            params: Dict = {k: v for k, v in params.items() if v is not None}

        extra_params: Dict = self._get_extra_params()
        headers: Dict = self._get_headers()
        response: requests.Response = requests.get(url, params, headers=headers, **extra_params)

        # 200 - OK
        if response.status_code != 200:
            raise Exception(response.status_code)

        return response

    @abstractmethod
    def _get_extra_params(self) -> Dict:
        return None

    @abstractmethod
    def _get_headers(self) -> Dict:
        return None

    @abstractmethod
    def _get_default_ttl(self) -> int:
        return None