import requests
import json
import pandas as pd
from steamid import SteamID
import csv
from steamid_converter import Converter
i = 1
with open("2021LabelsCulled4Final.csv", 'r') as data:
    with open("2021LabelsCulled4WithNames.csv", "w", newline="") as output:
        fieldnames = ['ID', "Label", "Count"]
        out = csv.DictWriter(output, fieldnames=fieldnames)
        out.writeheader()
        for line in csv.DictReader(data):

            print(str(i))
            i += 1
            # if i < 2800:
            #     continue
            # steamID = SteamID(line['ID'])
            # steamID64 = steamID.getSteamID64()
            # print(steamID.getSteamID64())

            steamID64 = Converter.to_steamID64(line['ID'], as_int=False)
            # print(steamID64)
            try:
                query = "{SearchPlayers(input: {steam64: \"" + str(steamID64) + "\"}) { name,steamId3,steam64}}"
                url = "https://demoticks.tf/graphQL"
                r = requests.post(url, json={'query':query})
                print(r.status_code)
                json_response = json.loads(r.text)
                # print(json_response['data']['SearchPlayers'][0]['name'])
                out.writerow({'ID': line['ID'], 'Label': json_response['data']['SearchPlayers'][0]['name'], 'Count': line['Count']})
                # print(r.status_code)
                # print(r.text)
            except:
                continue