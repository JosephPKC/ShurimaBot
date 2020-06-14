import datetime
from typing import Dict, List

from . import DataBase
from ..tools import Misc

class ChampionMastery(DataBase.DataBase):
    """ The data container for champion masteries.
    """
    def __init__(self, src: Dict) -> None:
        """ Constructor for the Champion Mastery data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.champion_points_until_next_level: int = src['championPointsUntilNextLevel'] # Zero means max level.
        self.chest_granted: bool = src['chestGranted']
        self.champion_id: int = src['championId']
        self.last_play_time: datetime.datetime = Misc.ms_to_datetime(src['lastPlayTime'])
        self.champion_level: int = src['championLevel']
        self.summoner_id: str = src['summonerId']
        self.champion_points: int = src['championPoints'] # Total number of champion points for this champion for player.
        self.champion_points_since_last_level: int = src['championPointsSinceLastLevel']
        self.tokens_earned: int = src['tokensEarned']

class ChampionMasteryList(DataBase.DataBase):
    """ The data container for the champion mastery list.
    """
    def __init__(self, src: List) -> None:
        """ Constructor for the Champion Mastery List data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.champion_masteries: Dict[ChampionMastery] = {s['championId']: ChampionMastery(s) for s in src} # Sends a list of champion mastery srcs.