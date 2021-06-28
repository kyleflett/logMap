# import urllib library
from collections import defaultdict
from typing import OrderedDict
from urllib.request import urlopen
  
# import json
import json
import time
import csv

url = "http://deeznuts.link/Tf2LogSearcher/logs/"
end = ".json"
index = 2900000

# response = urlopen(url + str(index) + end)
# data_json = json.loads(response.read())

individualDict = defaultdict(int)
pairDict = defaultdict(int)

startTime = time.time()
for x in range(1, 200, 1):
    fileName = "data" + str(x) + ".json"
    try:
        with open(fileName, 'w', encoding='utf-8') as f:
            response = urlopen(url + str(x) + end)
            data_json = json.loads(response.read())
            json.dump(data_json, f, ensure_ascii=False, indent=4)
    except:
        #stuff
        continue
endTime = time.time()
timeRun = str(endTime - startTime)
print(timeRun)