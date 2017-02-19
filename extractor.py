# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:04:00 2017

@author: JK Rutter
"""

import json
import requests
import numpy as np

f = open('static\matches1.json')

d = json.load(f)

summonerInfo = []
champs = []

for games in d['matches']:
    players = games['participantIdentities']
    plInfo = games['participants']
    sIds = []
    tiers = []
    for pl in players:
        sumId = pl['player']['summonerId']
        sIds.append(sumId)
    for pl in plInfo:
        tier = pl['highestAchievedSeasonTier']
        champ = pl['championId']
        champs.append(champ)
        tiers.append(tier)
    for i in range(0, len(sIds)):
        summonerInfo.append([sIds[i], tiers[i]])
    
"""
Champion Popularity
"""

champPlayed = [[0, 0]]

for i in range(0, len(champs)):
    found = False
    for j in range(0, len(champPlayed)):
        if champs[i] == champPlayed[j][0]:
            champPlayed[j][1] = champPlayed[j][1] + 1
            found = True
    if found == False:
        champPlayed.append([champs[i], 1])

for i in range(1, len(champPlayed)):
    champUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(champPlayed[i][0])+"?champData=info&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(champUrl)
    interpret = response.json()
    
    print(interpret['name'] + ": " + str(champPlayed[i][1]))