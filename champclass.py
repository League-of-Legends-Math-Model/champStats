# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:02:06 2016

@author: JK Rutter
"""
import json
import requests
import numpy as np

def statsFetcher(num):
    champUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(num) + "?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(champUrl)
    champ = response.json()
    baseStats = champ['stats']
    statsArray = np.zeros(shape =(20))
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
    