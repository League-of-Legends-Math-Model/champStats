# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:49:45 2017

@author: JK Rutter

Match Data Tests

22067266 - Masaana
2390295785 - Match ID
"""
import requests
import json
import numpy as np

matchId = 2390295785
matchURL = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchId)+"?includeTimeline=TRUE&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(matchURL)
matchdata = response.json()

frames = matchdata['timeline']['frames']
skillUps = np.zeros(shape=(10, 18))
levelCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in range(1, len(frames)):

    events = frames[i]['events']

    for j in range(0, len(events)):
        if events[j]['eventType'] == "SKILL_LEVEL_UP":
            if events[j]['levelUpType'] == "NORMAL":
                participant = events[j]['participantId'] - 1
                skill = events[j]['skillSlot']
                skillUps[participant][levelCount[participant]] = events[j]['skillSlot']
                levelCount[participant] = levelCount[participant] + 1

champstuff = []
#still building
particip = matchdata['participants']
for i in range(0, len(particip)):
    champstuff.append()
print(skillUps)
