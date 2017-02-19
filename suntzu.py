# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:58:58 2017

@author: Jon-Michael Rutter

Know The Enemy

"""

import requests
import json
import numpy as np
import datetime
import time


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
    
jmoId = "836619ee-c877-45d9-b718-ab0eea4ed172"

summonerName = input("Summoner: ")

summonerName = summonerName.lower()

summUrl = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(summUrl)
summerdata = response.json()

summonerID = summerdata[summonerName]['id']

currUrl = "https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/"+str(summonerID)+"?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(currUrl)
matchdata = response.json()
participants = matchdata['participants']

teams = []

for i in range(0, len(participants)):
    sId = participants[i]['summonerId']
    cId = participants[i]['championId']
    tId = participants[i]['teamId']
    nam = participants[i]['summonerName']
    teams.append([tId, sId, cId, nam])

for i in range(0, len(participants)):
    if participants[i]['summonerId'] == summonerID:
        champ = participants[i]['championId']
        team = participants[i]['teamId']

enTeam = []

for i in range(0, len(teams)):
    if team != teams[i][0]:
        enTeam.append(teams[i])

for i in range(0, len(enTeam)):
    phrase = str(i) + ": " + enTeam[i][3]
    print(phrase)

choice = input("Choose an opponent: ")

champ = enTeam[int(choice)][2]
summonerID = enTeam[int(choice)][1]

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

matches = []

timestamps = []
skillUps = []
items = []
kdas = []
killparticipation = []
wards = []
winloss = []
duration = []
levels = []
gold = []



if matchlist['totalGames'] > 0:
    for i in range(0, len(matchlist['matches'])):
        matchIds.append(matchlist['matches'][i]['matchId'])
        if i > 8:
            break;
    
    for i in range(0, len(matchIds)):
        time.sleep(2)
        matchUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(matchIds[i])+"?includeTimeline=TRUE&api_key=" + jmoId
        response = requests.get(matchUrl)
        matchHolder = response.json()
        
        matches.append(matchHolder)
    
    for i in range(0, len(matches)):
        timestamps.append(matches[i]['matchCreation'])
        duration.append(matches[i]['matchDuration'])
        participants = matches[i]['participants']

        itemSet = []
        highlight = 0
        matchKills = [0, 0]
        for j in range(0, len(participants)):
            if j < len(participants) / 2:
                matchKills[0] = matchKills[0] + participants[j]['stats']['kills']
            else:
                matchKills[1] = matchKills[1] + participants[j]['stats']['kills']
            if participants[j]['championId'] == champ:
                highlight = participants[j]['participantId']
                stats = participants[j]['stats']                
                levels.append(stats['champLevel'])
                kills = stats['kills']
                deaths = stats['deaths']
                assists = stats['assists']
                kdas.append([kills, deaths, assists])
                gold.append(stats['goldEarned'])
                itemSet.append(stats['item0'])
                itemSet.append(stats['item1'])
                itemSet.append(stats['item2'])
                itemSet.append(stats['item3'])
                itemSet.append(stats['item4'])
                itemSet.append(stats['item5'])
                itemSet.append(stats['item6'])
                winloss.append(stats['winner'])
                wards.append(stats['wardsPlaced'])
                items.append(itemSet)
        
        skilled = np.zeros(shape=(18))
        levelFr = 0
        frames = matches[i]['timeline']['frames']
        for k in range(1, len(frames)):
            events = frames[k]['events']
            for l in range(0, len(events)):
                if events[l]['eventType'] == "SKILL_LEVEL_UP":
                    if events[l]['levelUpType'] == "NORMAL":
                        if events[l]['participantId'] == highlight:
                            skilled[levelFr] = events[l]['skillSlot']
                            levelFr = levelFr + 1
        skillUps.append(skilled)
        
        if highlight < len(participants)/2 + 1:
            killparticipation.append(kills / matchKills[0])
        else:
            killparticipation.append(kills / matchKills[1])
    
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

    
    itemLikelihood = []
    
    for i in range(0, len(items)):
        for j in range(0, len(items[i])):
            if items[i][j] > 0:
                if len(itemLikelihood) == 0:
                    itemLikelihood.append([items[i][j], 1])
                else:
                    completed = False
                    for k in range(0, len(itemLikelihood)):
                        if itemLikelihood[k][0] == items[i][j]:
                            itemLikelihood[k][1] = itemLikelihood[k][1] + 1
                            completed = True
                    if completed == False:
                        itemLikelihood.append([items[i][j], 1])
                        

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
        try:
            itemLikelihood[i].append(itemstuff['name'])
        except:
            pass
        

    wins = 0
    for i in range(0, len(matches)):
        if winloss[i]:
            wins = wins + 1
    
    winrate = wins / len(matches)
    tehKda = [0, 0, 0]
    for i in range(0, len(kdas)):
        for j in range(0, 3):
            tehKda[j] = tehKda[j] + kdas[i][j]
    
    for i in range(0, 3):
        tehKda[i] = tehKda[i] / len(kdas)
        
    kp = 0
    
    for i in range(0, len(killparticipation)):
        kp = kp + killparticipation[i]
    
    kp / len(killparticipation)
    
    print(commonSkill)
    print(itemLikelihood)
    print("Winrate: " + str(winrate))
    print("Average Kills: " + str(tehKda[0]))
    print("Average Deaths: " + str(tehKda[1]))
    print("Average Assists: " + str(tehKda[2]))
    print("Average Kill Participation: " + str(kp))