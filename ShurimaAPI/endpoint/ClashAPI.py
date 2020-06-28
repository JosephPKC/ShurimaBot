from typing import Callable

from . import BaseRiotAPI
from ..data import Clash
from ..tools import Cache, Enums

class ClashAPI(BaseRiotAPI.BaseRiotAPI):
    """ ClashAPI handles the Riot API endpoints to retrieve champion masteries.
        https://developer.riotgames.com/apis#clash-v1
    """

    def __init__(self, cache: Cache.Cache, timeout: int, riot_key: str) -> None:
        """ Constructor for the Clash API.

        Args:
            cache (Cache.Cache): The cache manager.
            timeout (int): The amount of seconds to wait after sending a request before timing out.
            riot_key (str): The API key for riot's API.
        """
        super().__init__(cache, timeout, riot_key)

    def by_summoner_id(self, summoner_id: str, region: Enums.LOLRegion, ttl: int = None) -> Clash.ClashPlayerList:
        """ Retrieves the list of clash player infos based on summoner id.

        Args:
            summoner_id (str): The summoner id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            Clash.ClashPlayerList: The list of clash player infos.
        """
        method: str = f"clash/v1/players/by-summoner/{summoner_id}"
        url: str = self._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Clash.ClashPlayerList(r, True)

        return super().retrieve_data(url, builder, ttl=ttl)

    def by_team_id(self, team_id: str, region: Enums.LOLRegion, ttl: int = None) -> Clash.ClashTeam:
        """ Retrieves the clash team based on team id.

        Args:
            team_id (str): The team id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            Clash.ClashTeam: The clash team.
        """
        method: str = f"clash/v1/teams/{team_id}"
        url: str = self._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Clash.ClashTeam(r)

        return super().retrieve_data(url, builder, ttl=ttl)

    def all_tournaments(self, region: Enums.LOLRegion, ttl: int = None) -> Clash.ClashTournamentList:
        """ Retrieves all active clash tournaments.

        Args:
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            Clash.ClashTournamentList: The list of clash tournaments.
        """
        method: str = f"clash/v1/tournaments"
        url: str = self._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Clash.ClashTournamentList(r)

        return super().retrieve_data(url, builder, ttl=ttl)

    def tournament_by_team_id(self, team_id: str, region: Enums.LOLRegion, ttl: int = None) -> Clash.ClashTournament:
        """ Retrieves the tournament based on team id.

        Args:
            team_id (str): The team id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            Clash.ClashTournament: The clash tournament.
        """
        method: str = f"clash/v1/tournaments/by-team/{team_id}"
        url: str = self._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Clash.ClashTournament(r)

        return super().retrieve_data(url, builder, ttl=ttl)

    def tournament_by_tournament_id(self, tournament_id: str, region: Enums.LOLRegion, ttl: int = None) -> Clash.ClashTournament:
        """ Retrieves the tournament based on tournament id.

        Args:
            tournament_id (str): The tournament id to search for.
            region (Enums.LOLRegion): The region to check in.
            ttl (int, optional): The time to live. Defaults to None.

        Returns:
            Clash.ClashTournament: The clash tournament.
        """
        method: str = f"clash/v1/tournaments/{tournament_id}"
        url: str = self._get_riot_api_url(region.value, method)
        builder: Callable = lambda r: Clash.ClashTournament(r)

        return super().retrieve_data(url, builder, ttl=ttl)

    #region helpers
    def _get_default_ttl(self) -> int:
        return 1800 # Default to 30 minutes
    #endregion