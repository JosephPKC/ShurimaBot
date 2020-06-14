from typing import Dict, List

from . import common
from ..data import ChampionMastery, DataBase, Summoner

#region DataBase
def test_constructor_DataBase():
    src: Dict = common.test_summoner_json
    test_data_base: DataBase.DataBase = DataBase.DataBase(src)

    assert test_data_base is not None

def test___str__DataBase_return_str():
    src: Dict = common.test_summoner_json
    test_data_base: DataBase.DataBase = DataBase.DataBase(src)

    expected: str = ""
    actual: str = str(test_data_base)

    assert test_data_base is not None
    assert expected == actual
#endregion

#region ChampionMastery
def test_constructor_ChampionMastery():
    src: Dict = common.test_champion_mastery_json
    test_champion_mastery: ChampionMastery.ChampionMastery = ChampionMastery.ChampionMastery(src)

    assert test_champion_mastery is not None

def test_constructor_ChampionMasteryList():
    src: List = common.test_champion_mastery_list_json
    test_champion_mastery: ChampionMastery.ChampionMasteryList = ChampionMastery.ChampionMasteryList(src)

    assert test_champion_mastery is not None

def test___str___ChampionMastery_return_str():
    src: Dict = common.test_champion_mastery_json
    test_champion_mastery: ChampionMastery.ChampionMastery = ChampionMastery.ChampionMastery(src)

    expected: str = "champion_points_until_next_level: 1000, chest_granted: True, champion_id: 37, last_play_time: 1970-01-19 02:10:51.705000, champion_level: 5, " \
                    "summoner_id: test summoner id, champion_points: 1500, champion_points_since_last_level: 900, tokens_earned: 2"
    actual: str = str(test_champion_mastery)

    assert test_champion_mastery is not None
    assert expected == str(actual)
#endregion

#region Summoner
def test_constructor_Summoner():
    src: Dict = common.test_summoner_json
    test_summoner: Summoner.Summoner = Summoner.Summoner(src)

    assert test_summoner is not None

def test___str___Summoner_return_str():
    src: Dict = common.test_summoner_json
    test_summoner: Summoner.Summoner = Summoner.Summoner(src)
    
    expected: str = "account_id: test account id, profile_icon_id: 3587, revision_date: 1970-01-19 02:10:51.705000, " \
                    "name: test name, summoner_id: test summoner id, puu_id: test puu id, summoner_level: 144"
    actual: str = str(test_summoner)

    assert test_summoner is not None
    assert expected == actual
#endregion