from typing import Callable

from . import BaseRiotAPI
from ..data import ChampionMastery
from ..tools import Cache, Enums

class ChampionMasteryAPI(BaseRiotAPI.BaseRiotAPI):
    """ ChampionMasteryAPI handles the Riot API endpoints to retrieve champion masteries.
        https://developer.riotgames.com/apis#champion-mastery-v4
    """

    def __init__(self, cache: Cache.Cache, timeout: int, riot_key: str) -> None:
        """ Constructor for the Champion Mastery API.

        Args:
            cache (Cache.Cache): The cache manager.
            timeout (int): The amount of seconds to wait after sending a request before timing out.
            riot_key (str): The API key for riot's API.
        """
        super().__init__(cache, timeout, riot_key)

    def by_summoner_id(self, summoner_id: str, region: Enums.LOLRegion, ttl: int = None) -> ChampionMastery.ChampionMasteryList:
        """ Retrieves the list of champion masteries for the player.

        Args:
            summoner_id (str): The summoner id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            ChampionMastery.ChampionMasteryList: The list of champion masteries.
        """
        method: str = f"champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
        url: str = super()._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: ChampionMastery.ChampionMasteryList(r)

        return super().retrieve_data(url, builder, ttl=ttl)

    def by_summoner_id_by_champion_id(self, summoner_id: str, champion_id: int, region: Enums.LOLRegion, ttl: int = None) -> ChampionMastery.ChampionMastery:
        """ Retrieves the champion mastery for the specific champion for the player.

        Args:
            summoner_id (str): The summoner id to search for.
            champion_id (int): The champion id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            ChampionMastery.ChampionMastery: The champion mastery data container.
        """
        method: str = f"champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}"
        url: str = super()._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: ChampionMastery.ChampionMastery(r)

        return super().retrieve_data(url, builder, ttl=ttl)

    def total_by_summoner(self, summoner_id: str, region: Enums.LOLRegion, ttl: int = None) -> int:
        """ Retrieves the total champion mastery for the player.

        Args:
            summoner_id (str): The summoner id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            int: The total champion mastery.
        """
        method: str = f"champion-mastery/v4/scores/by-summoner/{summoner_id}"
        url: str = super()._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: r

        return super().retrieve_data(url, builder, ttl=ttl)

    #region helpers
    def _get_default_ttl(self) -> int:
        return 600 # Default to 10 minutes
    #endregion