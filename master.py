# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:09:50 2016

@author: JK Rutter
"""
import json
import requests
# itempull

dpsArray = [[[0, 0, 0, 0, 0, 0], 0]]
level = 3
gold = 1000

detBuilds = determinePossibleBuilds(gold)

cStats = caitStats(level)

for i in range(0, len(detBuilds)):
    stats = genChampionStatMatrix(cStats, detBuilds[i])
    items = detBuilds[i].getItems()
    print("st",stats);
    print("it",items);
    seq = caitAttackArray(stats, items)
    
    dps = calcDPS(seq)
    
    temp = [detBuilds[i].getItems(), dps]
    
    dpsArray.append([temp])

organize = [[0, 0]]

for i in range(0, len(dpsArray)):
    organize.append([dpsArray[i][1], i])

organize.sort(reverse=True)

print("Max DPS: " + str(organize[0][0]))

items = dpsArray[organize[0][1]][0]

for i in range(0, len(items)):
    itemurl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(int(items[i])) + "?itemData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(itemurl)
    buddy = response.json()
    name = buddy['name']
    print(name)
