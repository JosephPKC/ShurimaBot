import datetime
from typing import Dict, List

from . import DataBase
from ..tools import Enums, Misc

class ClashPlayer(DataBase.DataBase):
    def __init__(self, src: Dict, team_id: str = "") -> None:
        """ Constructor for the Clash player data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
            team_id (str, optional): The team id. If this is given, this will be used instead of the team id in the src.
        """
        super().__init__(src)

        self.summoner_id: str = src['summonerId']
        self.team_id: str = team_id if team_id != "" else src['teamId']
        self.position: Enums.LOLClashPosition = Enums.LOLClashPosition[src['position']]
        self.role: Enums.LOLClashRole = Enums.LOLClashRole[src['role']]

class ClashPlayerList(DataBase.DataBase):
    def __init__(self, src: List, is_all_same_players: bool, team_id: str = "") -> None:
        """ Constructor for the Clash Player List data container.

        Args:
            src (List): The source JSON from which the data container retrieves data from.
            is_all_same_players (bool): Whether the players in the list are all the same person or not.
            team_id (str, optional): The team id. If this is given, this will be used instead of the team id in the src.
        """
        super().__init__(src)

        # This flag determines how we structure the dict.
        # If this is all the same players, then we key off of the team id.
        # Otherwise, we key off of the summoner id.
        self.is_all_same_players: bool = is_all_same_players
        if is_all_same_players:
            self.clash_players: Dict[str, ClashPlayer] = {s['teamId']: ClashPlayer(s, team_id) for s in src} # Sends a list of clash player srcs.
        else:
            self.clas_players: Dict[str,ClashPlayer] = {s['summonerId']: ClashPlayer(s, team_id) for s in src} # Sends a list of clash player srcs.

class ClashTeam(DataBase.DataBase):
    def __init__(self, src: Dict) -> None:
        """ Constructor for the Clash Team data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.id: str = src['id']
        self.tournament_id: int = src['tournamentId']
        self.name: str = src['name']
        self.iconId: int = src['iconId']
        self.tier: int = src['tier']
        self.captain_id: str = src['captain'] # The summoner id of the team captain.
        self.abbreviation: str = src['abbreviation']
        self.players: ClashPlayerList = ClashPlayerList(src['players'], False, self.id) # A list of clash players for the team (different players)

class ClashTournament(DataBase.DataBase):
    def __init__(self, src: Dict) -> None:
        """ Constructor for the Clash Tournament data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.id: int = src['id']
        self.theme_id: int = src['themeId']
        self.name_key: str = src['nameKey']
        self.name_key_secondary: str = src['nameKeySecondary']
        self.schedule: Dict[int, ClashTournamentPhase] = {s['id']: ClashTournamentPhase(s) for s in src['schedule']}

class ClashTournamentList(DataBase.DataBase):
    def __init__(self, src: List) -> None:
        """ Constructor for the Clash Tournament List data container.

        Args:
            src (List): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.tournaments: Dict[int, ClashPlayer] = {s['id']: ClashTournament(s) for s in src}

class ClashTournamentPhase(DataBase.DataBase):
    def __init__(self, src: Dict) -> None:
        """ Constructor for the Clash Tournament Phase data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.id: int = src['id']
        self.registration_time: datetime.datetime = Misc.ms_to_datetime(src['registrationTime'])
        self.start_time: datetime.datetime = Misc.ms_to_datetime(src['startTime'])
        self.is_cancelled: bool = src['cancelled']