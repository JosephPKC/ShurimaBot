import datetime
from typing import Dict

from . import DataBase
from ..tools import Misc

class Summoner(DataBase.DataBase):
    """ The data container for summoners (players).
    """
    def __init__(self, src: Dict) -> None:
        """ Constructor for the Summoner data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        super().__init__(src)

        self.account_id: str = src['accountId'] # Encrypted
        self.profile_icon_id: int = src['profileIconId']
        self.revision_date: datetime.datetime = Misc.ms_to_datetime(src['revisionDate']) # May get a value error
        self.name: str = src['name']
        self.summoner_id: str = src['id']
        self.puu_id: str = src['puuid'] # Encrypted
        self.summoner_level: int = src['summonerLevel']