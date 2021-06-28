
# import urllib library
from collections import defaultdict
from typing import OrderedDict
from urllib.request import urlopen
  
# import json
import json
import time
import csv

# S6 EPOCH TIMES START: 5/17/2021 1621231200 END: 8/15/2021 1629093599
# S5 EPOCH TIMES START: 1/25/2021 1611558000 END: 4/25/2021 1619416799
# RGL ERA EPOCH TIMES START: 7/31/2019 1564552800 END: 6/26/2021 1624773599
# ESEA ERA EPOCH TIMES START: 11/18/2012 1353272955 1 END: 7/30/2019 1564552799 2340001
# 2021 EPOCH START: 1/1/2021 1609484400 2790001 END: 12/31/2021 1641020399 2890001
# 2020 EPOCH START: 1/1/2020 1577862000 2440001 END: 12/31/2020 1609484399 2790000
# 2019 EPOCH START: 1/1/2019 1546326000 2190001 END: 12/31/2019 1577861999 2440000
# 2018 EPOCH START: 1/1/2018 1514790000 1910001 END: 12/31/2018 1546325999  2190000
# 2017 EPOCH START: 1/1/2017 1483254000 1600001 END: 12/31/2017 1514789999 1910000
# 2016 EPOCH START: 1/1/2016 1451631600 1180001 END: 12/31/2016 1483253999 1600000
# 2015 EPOCH START: 1/1/2015 1420095600 610001 END: 12/31/2015 1451631599 1180000
# 2014 EPOCH START: 1/1/2014 1388559600 160001 END: 12/31/2014 1420095599 610000
# 2013 EPOCH START: 1/1/2013 1357023600 10001 END: 12/31/2013 1388559599 160000
# 2012 EPOCH START: 1/1/2012 1325401200 1 END: 12/31/2012 1357023599 10000

url = "http://deeznuts.link/Tf2LogSearcher/logs/"
end = ".json"

# Sample
# index = 2900000
# response = urlopen(url + str(index) + end)
# data_json = json.loads(response.read())

individualDict = defaultdict(int)
pairDict = defaultdict(int)

startTime = time.time()
with open('2021Labels.csv', 'w', newline='') as csvfile:
    fieldnames = ['steam_id', 'steam_id', 'count']
    labels = csv.DictWriter(csvfile, fieldnames=fieldnames)
    labels.writeheader()
    with open('2021Edges.csv', 'w', newline='') as csvfile2:
        fieldnames2 = ['steam_id1', 'steam_id2', 'count']
        edges = csv.DictWriter(csvfile2, fieldnames=fieldnames2)
        edges.writeheader()

        

        for x in range(1, 200, 1):
            try:
                # used for URL download
                # response = urlopen(url + str(x) + end)
                # data_json = json.loads(response.read())
                f = open('data' + str(x) + '.json',)
                data_json = json.load(f)
                print("Progress: Starting Log " + str(x) + " out of 1000")
                playersInLog = len(data_json["names"].keys())
                idList = list(data_json["names"].keys())
                nameList = list(data_json["names"].values())
                if playersInLog == 13 or playersInLog == 12:
                    # Creating an empty dictionary
                    for i in range(playersInLog):
                        
                        # add one to individual dict
                        individualDict[idList[i]] += 1
                        j = i + 1
                        while j < playersInLog:
                            # print(idList[i] + ': ' + nameList[i] + ', ' + idList[j] + ': ' + nameList[j])
                            id = tuple([idList[i], idList[j]])
                            idReversed = tuple([idList[i], idList[j]])
                            if pairDict[id] > 0:
                                pairDict[id] += 1
                            else:
                                pairDict[idReversed] += 1
                            # writer.writerow({'id': x, 'date': data_json['info']['date']})
                            j = j + 1
                    
            except:
                #maybe do something
                continue
        for key, value in individualDict.items():
            labels.writerow({'steam_id': key, 'steam_id': key, 'count': value})
        for key, value in pairDict.items():
            edges.writerow({'steam_id1': key[0], 'steam_id2': key[1], 'count': value})
endTime = time.time()
result = str(startTime) + " " + str(endTime)
timeRun = str(endTime - startTime)
print(timeRun)

# the steamids are found at data_json["names"].keys()
# the length is len(data_json["names"].keys())
# The date is data_json['info']['date']
# print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data_json['info']['date'])))
# print(data_json['info']['date'])

# json_object = json.loads(data_json)
# json_formatted_str = json.dumps(json_object, indent=2)

# print(json_formatted_str)