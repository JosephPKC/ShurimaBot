
# This will just be to test and run while coding.
# This is an API wrapper, so there is no entry point, other than core.
# Actual unit tests should be under test.

import json
import requests
import time

from ShurimaAPI import Shurima
from ShurimaAPI.data import Summoner
from ShurimaAPI.tools.Enums import LOL
# Get the riot api key
global riot_api_key

with open("config.json") as f:
    config = json.load(f)

    try:
        riot_api_key = config['keys']['riot']
    except KeyError:
        riot_api_key = ""
        print("'keys' does not exist in config.json. Please check that it is formatted properly.")

print("riot api: ", riot_api_key)

api = Shurima.Shurima(30, riot_api_key)


print("----- TESTING SUMMONER API -----")
result: Summoner.Summoner = api.Summoner.by_name("GetOut", LOL.Region.NA)
print(result)
result = api.Summoner.by_account_id(result.account_id, LOL.Region.NA)
print(result)
result = api.Summoner.by_puu_id(result.puu_id, LOL.Region.NA)
print(result)
result = api.Summoner.by_summoner_id(result.summoner_id, LOL.Region.NA)
print(result)

print("Second time ------")
result = api.Summoner.by_name("AtuhorsNosePKC", LOL.Region.NA)
print(result)
result = api.Summoner.by_account_id(result.account_id, LOL.Region.NA)
print(result)
result = api.Summoner.by_puu_id(result.puu_id, LOL.Region.NA)
print(result)
result = api.Summoner.by_summoner_id(result.summoner_id, LOL.Region.NA)
print(result)

# print("Testing expiration ------")
# time.sleep(10)
# result = api.Summoner.by_name("AtuhorsNosePKC", LOL.Region.NA)
# print(result)

# Store summoner id for future tests
summoner_id = result.summoner_id

print("----- TESTING CHAMPION MASTERY API -----")
result = api.ChampionMastery.by_summoner_id(summoner_id, LOL.Region.NA)
print(result)
result = api.ChampionMastery.by_summoner_id_by_champion_id(summoner_id, 1, LOL.Region.NA)
print(result)
result = api.ChampionMastery.total_by_summoner_id(summoner_id, LOL.Region.NA)
print(result)

print("Second time -----")
result = api.ChampionMastery.by_summoner_id(summoner_id, LOL.Region.NA)
print(result)
result = api.ChampionMastery.by_summoner_id_by_champion_id(summoner_id, 1, LOL.Region.NA)
print(result)
result = api.ChampionMastery.total_by_summoner_id(summoner_id, LOL.Region.NA)
print(result)

# print("----- TESTING CLASH API -----")
# clashers = api.Clash.by_summoner_id(summoner_id, LOL.Region.NA)
# print(result)
# result = api.Clash.by_team_id(list(clashers.clash_players)[0].team_id, LOL.Region.NA)
# print(result)

# print("Second time -----")
# clashers = api.Clash.by_summoner_id(summoner_id, LOL.Region.NA)
# print(result)
# result = api.Clash.by_team_id(list(clashers.clash_players)[0].team_id, LOL.Region.NA)
# print(result)
