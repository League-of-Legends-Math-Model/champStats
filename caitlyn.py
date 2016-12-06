# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:49:19 2016

@author: JK Rutter
"""

import requests
import json
import numpy as np

def growth(charBase, charGrowth, level):
    return charBase + charGrowth * (level - 1) * (0.685 + 0.0175 * level)

def caitStats(lvl):
    caitUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/51?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(caitUrl)
    cait = response.json()
    baseStats = cait['stats']
    caitStat = np.zeros(shape=(2, 9))
    caitStat[0][0] = baseStats['hp']
    caitStat[0][1] = baseStats['hpregen']
    caitStat[0][2] = baseStats['armor']
    caitStat[0][3] = baseStats['spellblock']
    caitStat[0][4] = baseStats['attackdamage']
    caitStat[0][8] = 0.625 / (1 + baseStats['attackspeedoffset'])
    caitStat[1][0] = baseStats['hpperlevel']
    caitStat[1][1] = baseStats['hpregenperlevel']
    caitStat[1][2] = baseStats['armorperlevel']
    caitStat[1][3] = baseStats['spellblockperlevel']
    caitStat[1][4] = baseStats['attackdamageperlevel']
    caitStat[1][5] = baseStats['attackspeedperlevel'] / 100
    endStat = np.zeros(shape=(10))
    for i in range(0, 8):
        endStat[i] = growth(caitStat[0][i], caitStat[1][i], lvl)
    endStat[8] = caitStat[0][8]
    endStat[9] = lvl
    endStat[5] = endStat[8] + endStat[8] * endStat[5]
    print(endStat)
    return endStat

charStat = caitStats(18)

print(charStat)