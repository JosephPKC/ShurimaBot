from typing import Dict

from . import common
from ..endpoint import ChampionMasteryAPI, SummonerAPI
from ..tools import Cache
from ..tools.Enums import LOL

# Note: BaseAPI and BaseRiotAPI are not completely tested as they are abstract.

#region BaseRiotAPI
def test__get_extra_params_BaseRiotAPI_return_dict():
    cache: Cache.Cache = Cache.Cache()
    timeout: int = 0
    riot_key: str = "" # Not used in test
    # Using the ChampionMasteryAPI to test the BaseRiotAPI methods.
    test_champion_mastery_api: ChampionMasteryAPI.ChampionMasteryAPI = ChampionMasteryAPI.ChampionMasteryAPI(cache, timeout, riot_key)

    expected: Dict = {
        'timeout': timeout
    }
    actual: Dict = test_champion_mastery_api._get_extra_params()

    assert expected == actual

def test__get_headers_BaseRiotAPI_return_dict():
    cache: Cache.Cache = Cache.Cache()
    timeout: int = 0
    riot_key: str = "test" # Not used in test
    # Using the ChampionMasteryAPI to test the BaseRiotAPI methods.
    test_champion_mastery_api: ChampionMasteryAPI.ChampionMasteryAPI = ChampionMasteryAPI.ChampionMasteryAPI(cache, timeout, riot_key)

    expected: Dict = {
        'X-Riot-Token': riot_key
    }
    actual: Dict = test_champion_mastery_api._get_headers()

    assert expected == actual
#endregion

#region ChampionMasteryAPI
def test_constructor_ChampionMasteryAPI():
    cache: Cache.Cache = Cache.Cache()
    timeout: int = 0
    riot_key: str = "" # Not used in test
    test_champion_mastery_api: ChampionMasteryAPI.ChampionMasteryAPI = ChampionMasteryAPI.ChampionMasteryAPI(cache, timeout, riot_key)

    assert test_champion_mastery_api is not None

def test__get_default_ttl_ChampionMasteryAPI_return_num():
    cache: Cache.Cache = Cache.Cache()
    timeout: int = 0
    riot_key: str = "test" # Not used in test
    test_champion_mastery_api: ChampionMasteryAPI.ChampionMasteryAPI = ChampionMasteryAPI.ChampionMasteryAPI(cache, timeout, riot_key)

    expected: int = 600
    actual: Dict = test_champion_mastery_api._get_default_ttl()

    assert expected == actual
#endregion

#region SummonerAPI
def test_constructor_SummonerAPI():
    cache: Cache.Cache = Cache.Cache()
    timeout: int = 0
    riot_key: str = "" # Not used in test
    test_summoner_api: SummonerAPI.SummonerAPI = SummonerAPI.SummonerAPI(cache, timeout, riot_key)

    assert test_summoner_api is not None

def test__get_default_ttl_SummonerAPI_return_num():
    cache: Cache.Cache = Cache.Cache()
    timeout: int = 0
    riot_key: str = "test" # Not used in test
    test_summoner_api: SummonerAPI.SummonerAPI = SummonerAPI.SummonerAPI(cache, timeout, riot_key)

    expected: int = 600
    actual: Dict = test_summoner_api._get_default_ttl()

    assert expected == actual
#endregion