# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:04:50 2017

@author: Jon-Michael

22067266 - Masaana
"""

import requests
import json
import numpy as np
import datetime

summonerID = 22067266
champ = 51

listUrl = "https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/"+str(summonerID)+"?championIds="+str(champ)+"&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(listUrl)
matchlist = response.json()

matchInfo = []

if matchlist['totalGames'] > 0:
    for i in range(0, len(matchlist['matches'])):
        matchInfo.append([matchlist['matches'][i]['matchId'], matchlist['matches'][i]['timestamp']])
    for i in range(0, len(matchInfo)):
        timer = matchInfo[i][1] / 1000
        matchInfo[i].append(datetime.datetime.fromtimestamp(timer).strftime('%Y-%m-%d %H:%M'))

currtime = datetime.datetime.now()
then = datetime.datetime.fromtimestamp(matchInfo[len(matchInfo)-1][1]/1000)

difference = currtime - then

print(difference)