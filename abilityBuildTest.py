# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:32:09 2017

@author: JK Rutter

22067266 - Masaana
2390295785 - Match ID
45605158 - Cabiano
47584599 - rainbow dashOP
45754832 - derakos

api keys
444a50cf-4457-4339-8f70-2369dbd09b18 - Max
836619ee-c877-45d9-b718-ab0eea4ed172 - Jon-Michael

10 calls every 10 seconds; 500 calls every 10 minutes

"""

import requests
import json
import numpy as np

def abRules(skillOrder, slot, skill, chId):
    ready = True
    soFar = [0, 0, 0, 0]
    skillCap = 5
    ultSkillCap = 3
    if chId == 77:
        ultSkillCap = 5
        
    if chId == 126:
        skillCap = 6
    for p in range(0, slot):
        soFar[int(skillOrder[p])] = soFar[int(skillOrder[p])] + 1
    
    #Rule for 2nd slot
    if slot == 1:
        if skill == skillOrder[0]:
            ready = False
    if slot == 3:
        if soFar[skill] == 2:
            ready = False
    if slot == 7:
        if soFar[skill] == 4:
            ready = False
    if slot > 8:
        if soFar[skill] == skillCap:
            ready = False
        if skill == 3 and soFar[skill] == ultSkillCap:
            ready = False

    return ready

maxId = "444a50cf-4457-4339-8f70-2369dbd09b18"
jmoId = "836619ee-c877-45d9-b718-ab0eea4ed172"

#level thresholds = [top, jungle, mid, bot, support]
thresholds = [16, 15, 16, 15, 12]

summonerName = input("Summoner: ")

summonerName = summonerName.lower()
#1 call
summUrl = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(summUrl)
summerdata = response.json()



summonerID = summerdata[summonerName]['id']

#2 call
currUrl = "https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/"+str(summonerID)+"?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(currUrl)
matchdata = response.json()
participants = matchdata['participants']

#looking for the chosen summoner's ability sequence history and item build
for i in range(0, len(participants)):
    if participants[i]['summonerId'] == summonerID:
        champ = participants[i]['championId']

#this call doesn't count
champUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(champ)+"?champData=info&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(champUrl)
champInfo = response.json()
print(champInfo['name'])

#3 call
listUrl = "https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/"+str(summonerID)+"?championIds="+str(champ)+"&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(listUrl)
matchlist = response.json()

matchIds = []

skillUps = []
itemList = []


if matchlist['totalGames'] > 0:
    for i in range(0, len(matchlist['matches'])):
        matchIds.append(matchlist['matches'][i]['matchId'])

    
    for i in range(0, len(matchIds)):
        uncertain = True
        odd = True
        atNext = 1
        while uncertain:
            if (i + 1) / (10 * atNext) < 1:
                if odd:
                    matchUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchIds[i])+"?includeTimeline=TRUE&api_key=" + maxId
                else:
                    matchUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchIds[i])+"?includeTimeline=TRUE&api_key=" + jmoId
                uncertain = False
            if odd:
                odd = False
            else:
                odd = True
            atNext = atNext + 1
        
        response = requests.get(matchUrl)
        matchstuff = response.json()

        players = matchstuff['participants']

        highlight = 0
        level = 0
        
        item0 = 0
        item1 = 0
        item2 = 0
        item3 = 0
        item4 = 0
        item5 = 0
        item6 = 0
        for j in range(0, len(players)):
            if players[j]['championId'] == champ:
                highlight = players[j]['participantId']
                level = players[j]['stats']['champLevel']
                item0 = players[j]['stats']['item0']
                item1 = players[j]['stats']['item1']
                item2 = players[j]['stats']['item2']
                item3 = players[j]['stats']['item3']
                item4 = players[j]['stats']['item4']
                item5 = players[j]['stats']['item5']
                item6 = players[j]['stats']['item6']
                

        if level > 15:
            itemList.append([item0, item1, item2, item3, item4, item5, item6])  
            skilled = np.zeros(shape=(18))
            levelFr = 0
            frames = matchstuff['timeline']['frames']
            for k in range(1, len(frames)):
                events = frames[k]['events']
                for l in range(0, len(events)):
                    if events[l]['eventType'] == "SKILL_LEVEL_UP":
                        if events[l]['levelUpType'] == "NORMAL":
                            if events[l]['participantId'] == highlight:
                                skilled[levelFr] = events[l]['skillSlot']
                                levelFr = levelFr + 1
            skillUps.append(skilled)
             

    skillSet = np.zeros(shape=(4, 18))
    
    for i in range(0, len(skillUps)):
        for j in range(0, len(skillUps[i])):        
            sk = skillUps[i][j]
            skillSet[int(sk - 1)][j] = skillSet[int(sk - 1)][j] + 1

    commonSkill = np.zeros(shape=(18))

    for i in range(0, len(commonSkill)):
        expected = 0
        nExpected = 0
        times = 0
        nTimes = 0        
        for j in range(0, len(skillSet)):
            if skillSet[j][i] > times:
                nTimes = times
                nExpected = expected
                expected = j
                times = skillSet[j][i]
        works = abRules(commonSkill, i, expected, champ)
        if works:        
            commonSkill[i] = expected
        else:
            commonSkill[i] = nExpected

    print(commonSkill)
    
    itemLikelihood = []
    
    for i in range(0, len(itemList)):
        for j in range(0, len(itemList[i])):
            if itemList[i][j] > 0:
                if len(itemLikelihood) == 0:
                    itemLikelihood.append([itemList[i][j], 1])
                else:
                    completed = False
                    for k in range(0, len(itemLikelihood)):
                        if itemLikelihood[k][0] == itemList[i][j]:
                            itemLikelihood[k][1] = itemLikelihood[k][1] + 1
                            completed = True
                    if completed == False:
                        itemLikelihood.append([itemList[i][j], 1])
                        

    for i in range(0, len(itemLikelihood) - 1):
        for j in range(i + 1, len(itemLikelihood)):
            if itemLikelihood[i][1] < itemLikelihood[j][1]:
                store = itemLikelihood[i]
                itemLikelihood[i] = itemLikelihood[j]
                itemLikelihood[j] = store

    for i in range(0, len(itemLikelihood)):
        itemUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(itemLikelihood[i][0])+"?itemData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
        response = requests.get(itemUrl)
        itemstuff = response.json()
        
        itemLikelihood[i].append(itemstuff['name'])
    
    print(itemLikelihood)
    
"""
while unfound:
    matchUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchIds[i])+"?includeTimeline=TRUE&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
"""