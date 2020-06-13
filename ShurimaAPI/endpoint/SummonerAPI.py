from typing import Callable

from . import BaseRiotAPI
from ..data import Summoner
from ..tools import Cache, Enums

class SummonerAPI(BaseRiotAPI.BaseRiotAPI):
    """ SummonerAPI is the Riot API endpoint to retrieve player information.
    """
    def __init__(self, cache: Cache.Cache, timeout: int, riot_key: str) -> None:
        """ Constructor for the Summoner API.

        Args:
            cache (Cache.Cache): The cache manager.
            timeout (int): The amount of seconds to wait after sending a request before timing out.
            riot_key (str): The API key for riot's API.
        """
        super().__init__(cache, timeout, riot_key)

    def by_name(self, summoner_name: str, region: Enums.LOLRegion, ttl: int = None) -> object:
        """ Retrieves player information by name.

        Args:
            summoner_name (str): The name of the player.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            object: The summoner data container.
        """
        method: str = f"summoner/v4/summoners/by-name/{summoner_name}"
        return self.__retrieve_summoner_data(method, region, ttl)

    def by_account_id(self, account_id: str, region: Enums.LOLRegion, ttl: int = None) -> object:
        """ Retrieves player information by account id.

        Args:
            account_id (str): The account id of the player.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            object: The summoner data container.
        """
        method: str = f"summoner/v4/summoners/by-account/{account_id}"
        return self.__retrieve_summoner_data(method, region, ttl)

    def by_puu_id(self, puu_id: str, region: Enums.LOLRegion, ttl: int = None) -> object:
        """ Retrieves player information by puu id.

        Args:
            puu_id (str): The puu id of the player.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            object: The summoner data container.
        """
        method: str = f"summoner/v4/summoners/by-puuid/{puu_id}"
        return self.__retrieve_summoner_data(method, region, ttl)

    def by_summoner_id(self, summoner_id: str, region: Enums.LOLRegion, ttl: int = None) -> object:
        """ Retrieves player information by summoner id.

        Args:
            summoner_id (str): The summoner id of the player.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            object: The summoner data container.
        """
        method: str = f"summoner/v4/summoners/{summoner_id}"
        return self.__retrieve_summoner_data(method, region, ttl)

    #region helpers
    def __retrieve_summoner_data(self, method: str, region: Enums.LOLRegion, ttl: int) -> object:
        url: str = super()._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Summoner.Summoner(r)

        return super().retrieve_data(url, builder, ttl=ttl)
    
    def _get_default_ttl(self) -> int:
        return 600 # Default to 10 minutes
    #endregion