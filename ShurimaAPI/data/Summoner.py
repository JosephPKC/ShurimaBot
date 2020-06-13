import datetime
from typing import Dict

from . import DataBase

class Summoner(DataBase.DataBase):
    def __init__(self, src: Dict) -> None:
        super().__init__(src)

        self.account_id: str = src['accountId'] # Encrypted
        self.profile_icon_id: int = src['profileIconId']
        self.revision_date: datetime.datetime = datetime.datetime.fromtimestamp(src['revisionDate']/1000.0) # May get a value error
        self.name: str = src['name']
        self.id: str = src['id']
        self.puu_id: str = src['puuid'] # Encrypted
        self.summoner_level: int = src['summonerLevel']