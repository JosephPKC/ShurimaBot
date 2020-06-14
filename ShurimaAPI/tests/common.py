from typing import Dict, List

#region test JSONs
test_champion_mastery_json: Dict = {
    'championPointsUntilNextLevel': 1000,
    'chestGranted': True,
    'championId': 37,
    'lastPlayTime': 1591851705,
    'championLevel': 5,
    'summonerId': "test summoner id",
    'championPoints': 1500,
    'championPointsSinceLastLevel': 900,
    'tokensEarned': 2
}

test_champion_mastery_list_json: List = [
    {
        'championPointsUntilNextLevel': 1000,
        'chestGranted': True,
        'championId': 37,
        'lastPlayTime': 1591851705,
        'championLevel': 5,
        'summonerId': "test summoner id",
        'championPoints': 1500,
        'championPointsSinceLastLevel': 900,
        'tokensEarned': 2
    },
    {
        'championPointsUntilNextLevel': 2000,
        'chestGranted': False,
        'championId': 38,
        'lastPlayTime': 1591851705,
        'championLevel': 8,
        'summonerId': "test summoner id",
        'championPoints': 3000,
        'championPointsSinceLastLevel': 5000,
        'tokensEarned': 4
    },
]

test_summoner_json: Dict = {
    'id': "test summoner id",
    'accountId': "test account id",
    'puuid': "test puu id",
    'name': "test name",
    'profileIconId': 3587,
    'revisionDate': 1591851705,
    'summonerLevel': 144
}
#endregion

#region test responses
test_summoner_response: str = "{" \
    "\"id\": \"test summoner id\", " \
    "\"accountId\": \"test account id\", " \
    "\"puuid\": \"test puu id\", " \
    "\"name\": \"test name\", " \
    "\"profileIconId\": 3587, " \
    "\"revisionDate\": 1591851705, " \
    "\"summonerLevel\": 144" \
    "}"
#endregion