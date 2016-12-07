# -*- coding: utf-8 -*-
"""
Created on Wed Dec 7 10:37:19 2016

@author: JK Rutter
"""

import requests
import json
import numpy as np

def growth(charBase, charGrowth, level):
    return charBase + charGrowth * (level - 1) * (0.685 + 0.0175 * level)

def sivirStats(lvl):
    sivirUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/15?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(sivirUrl)
    sivir = response.json()
    baseStats = sivir['stats']
    sivirStat = np.zeros(shape=(2, 9))
    sivirStat[0][0] = baseStats['hp']
    sivirStat[0][1] = baseStats['hpregen']
    sivirStat[0][2] = baseStats['armor']
    sivirStat[0][3] = baseStats['spellblock']
    sivirStat[0][4] = baseStats['attackdamage']
    sivirStat[0][8] = 0.625 / (1 + baseStats['attackspeedoffset'])
    sivirStat[1][0] = baseStats['hpperlevel']
    sivirStat[1][1] = baseStats['hpregenperlevel']
    sivirStat[1][2] = baseStats['armorperlevel']
    sivirStat[1][3] = baseStats['spellblockperlevel']
    sivirStat[1][4] = baseStats['attackdamageperlevel']
    sivirStat[1][5] = baseStats['attackspeedperlevel'] / 100
    endStat = np.zeros(shape=(10))
    for i in range(0, 8):
        endStat[i] = growth(sivirStat[0][i], sivirStat[1][i], lvl)
    endStat[8] = sivirStat[0][8]
    endStat[9] = lvl
    endStat[5] = endStat[8] + endStat[8] * endStat[5]
    print(endStat)
    return endStat

charStat = sivirStats(18)

print(charStat)