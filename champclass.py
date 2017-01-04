# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:02:06 2016

@author: JK Rutter

Base Stats:
    0 - HP
    1 - HPPERLEVEL
    2 - HPREGEN
    3 - HPREGENPERLEVEL
    4 - MP
    5 - MPPERLEVEL
    6 - MPREGEN
    7 - MPREGENPERLEVEL
    8 - ATTACKDAMAGE
    9 - ATTACKDAMAGEPERLEVEL
    10 - ATTACK RANGE
    11 - CRIT
    12 - CRITPERLEVEL
    13 - ATTACKSPEEDOFFSET
    14 - ATTACKSPEEDPERLEVEL
    15 - ARMOR
    16 - ARMORPERLEVEL
    17 - SPELLBLOCK (mr)
    18 - SPELLBLOCKPERLEVEL
    19 - MOVESPEED
-------------------------------------
    20 - ABILITY POWER
    21 - ABILITY POWER PER LEVEL
    22 - LETHALITY
    23 - ARMOR PEN
    24 - % ARMOR PEN
    25 - MAGIC PEN
    26 - % MAGIC PEN
    27 - TENACITY
    28 - SLOW RESIST
    29 - COOLDOWN REDUCTION
    30 - LIFESTEAL
    31 - SPELLVAMP
    32 - BASE PERCENT MITIGATION
    33 - BASE PERCENT ABILITY INCREASE
    34 - BASE PERCENT ALL DAMAGE INCREASE
"""
import json
import requests
import numpy as np

def statsFetcher(num):
    champUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(num) + "?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(champUrl)
    champ = response.json()
    baseStats = champ['stats']
    statsArray = np.zeros(shape =(32))
    statsArray[0] = baseStats['hp']
    statsArray[1] = baseStats['hpperlevel']
    statsArray[2] = baseStats['hpregen']
    statsArray[3] = baseStats['hpregenperlevel']
    statsArray[4] = baseStats['mp']
    statsArray[5] = baseStats['mpperlevel']
    statsArray[6] = baseStats['mpregen']
    statsArray[7] = baseStats['mpregenperlevel']
    statsArray[8] = baseStats['attackdamage']
    statsArray[9] = baseStats['attackdamageperlevel']
    statsArray[10] = baseStats['attackrange']
    statsArray[11] = baseStats['crit']
    statsArray[12] = baseStats['critperlevel']
    statsArray[13] = baseStats['attackspeedoffset']
    statsArray[14] = baseStats['attackspeedperlevel']
    statsArray[15] = baseStats['armor']
    statsArray[16] = baseStats['armorperlevel']
    statsArray[17] = baseStats['spellblock']
    statsArray[18] = baseStats['spellblockperlevel']
    statsArray[19] = baseStats['movespeed']
    return statsArray

def growth(charBase, charGrowth, level):
    return charBase + charGrowth * (level - 1) * (0.685 + 0.0175 * level)


class champion():
    