# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:16:19 2016

@author: JK Rutter
"""

import requests
import json
import numpy as np

def growth(charBase, charGrowth, level):
    return charBase + charGrowth * (level - 1) * (0.685 + 0.0175 * level)

def quinnStats(lvl):
    quinnUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/133?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(quinnUrl)
    quinn = response.json()
    baseStats = quinn['stats']
    quinnStat = np.zeros(shape=(2, 9))
    quinnStat[0][0] = baseStats['hp']
    quinnStat[0][1] = baseStats['hpregen']
    quinnStat[0][2] = baseStats['armor']
    quinnStat[0][3] = baseStats['spellblock']
    quinnStat[0][4] = baseStats['attackdamage']
    quinnStat[0][8] = 0.625 / (1 + baseStats['attackspeedoffset'])
    quinnStat[1][0] = baseStats['hpperlevel']
    quinnStat[1][1] = baseStats['hpregenperlevel']
    quinnStat[1][2] = baseStats['armorperlevel']
    quinnStat[1][3] = baseStats['spellblockperlevel']
    quinnStat[1][4] = baseStats['attackdamageperlevel']
    quinnStat[1][5] = baseStats['attackspeedperlevel'] / 100
    endStat = np.zeros(shape=(10))
    for i in range(0, 8):
        endStat[i] = growth(quinnStat[0][i], quinnStat[1][i], lvl)
    endStat[8] = quinnStat[0][8]
    endStat[9] = lvl
    endStat[5] = endStat[8] + endStat[8] * endStat[5]
    print(endStat)
    return endStat

charStat = quinnStats(18)

print(charStat)