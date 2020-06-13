
# This will just be to test and run while coding.
# This is an API wrapper, so there is no entry point, other than core.
# Actual unit tests should be under test.

import json
import requests

from ShurimaAPI import Shurima
from ShurimaAPI.data import Summoner
from ShurimaAPI.tools import Enums
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
result: Summoner.Summoner = api.Summoner.by_name("AtuhorsNosePKC", Enums.LOLRegion.NA)
print(result)
result = api.Summoner.by_account_id(result.account_id, Enums.LOLRegion.NA)
print(result)