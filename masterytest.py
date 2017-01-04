# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:52:43 2016

@author: JK Rutter
"""

import json
import requests

""" FOR RUNES / MASTERIES LATER
for itmAtr in (list(itemStats.items())):
            ##all possibilities for item boost
            if(itmAtr[0]=="FlatArmorMod"):
                newChampStat[ARMOR] = newChampStat[ARMOR]+itmAtr[1];
            if(itmAtr[0]=="FlatAttackSpeedMod"):
                newChampStat[ATTACK_SPEED] = newChampStat[ATTACK_SPEED]+itmAtr[1]
            if(itmAtr[0]=="FlatBlockMod"):
                print(-99);  #ToDO
            if(itmAtr[0]=="FlatCritChanceMod"):
                newChampStat[CRIT_STRIKE] = newChampStat[CRIT_STRIKE]+itmAtr[1]
            if(itmAtr[0]=="FlatCritDamageMod"):
                print(-99);  #ToDO
            if(itmAtr[0]=="FlatEXPBonus"):
                print(-99);  #ToDO
            if(itmAtr[0]=="FlatEnergyPoolMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="FlatEnergyRegenMod"):
                print(-99);  #ToDO
            if(itmAtr[0]=="FlatHPPoolMod"):
                newChampStat[HEALTH] = newChampStat[HEALTH]+itmAtr[1]
            if(itmAtr[0]=="FlatHPRegenMod"):
                newChampStat[HEALTH_REGEN] = newChampStat[HEALTH_REGEN]+itmAtr[1]
            if(itmAtr[0]=="FlatMPPoolMod"):
                print(-99);  #ToDO
            if(itmAtr[0]=="FlatMPRegenMod"):
                print(-99);  #ToDO
            if(itmAtr[0]=="FlatMagicDamageMod"):
                print(-99);  #ToDO                
            if(itmAtr[0]=="FlatMovementSpeedMod"):
                print(-99);
            if(itmAtr[0]=="FlatPhysicalDamageMod"):
                newChampStat[ATTACK_DAMADGE] = newChampStat[ATTACK_DAMADGE]+itmAtr[1]
            if(itmAtr[0]=="FlatSpellBlockMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentArmorMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentAttackSpeedMod"):
                newChampStat[ATTACK_SPEED] = newChampStat[ATTACK_SPEED]+(newChampStat[ATTACK_SPEED_OFFSET]*itmAtr[1]);
            if(itmAtr[0]=="PercentCritChanceMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentCritDamageMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentDodgeMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentEXPBonus"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentHPPoolMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentHPRegenMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentLifeStealMod"):
                newChampStat[LIFE_STEAL] = newChampStat[LIFE_STEAL]+(itmAtr[1]);
            if(itmAtr[0]=="PercentMPPoolMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentMPRegenMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentMagicDamageMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentMovementSpeedMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentPhysicalDamageMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentSpellBlockMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="PercentSpellVampMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatArmorModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatArmorPenetrationMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatArmorPenetrationModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatCritChanceModPerLevel"):
                print(-99);  #ToDO                 
            if(itmAtr[0]=="rFlatCritDamageModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatDodgeMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatDodgeModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatEnergyModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatEnergyRegenModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatGoldPer10Mod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatArmorPenetrationModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatHPRegenModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatMPModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatMPRegenModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatMagicDamageModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatMagicPenetrationMod"):
                print(-99);  #ToDO                 
            if(itmAtr[0]=="rFlatMagicPenetrationModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatMovementSpeedModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatPhysicalDamageModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatSpellBlockModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatTimeDeadMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rFlatTimeDeadModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentArmorPenetrationMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentArmorPenetrationModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentAttackSpeedModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentCooldownMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentCooldownModPerLevel"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentMagicPenetrationMod"):
                print(-99);  #ToDO 
            if(itmAtr[0]=="rPercentMagicPenetrationModPerLevel"):
                print(itmAtr[1]);
            if(itmAtr[0]=="rPercentMovementSpeedModPerLevel"):
                print(-99);
            if(itmAtr[0]=="rPercentTimeDeadMod"):
                print(-99);
            if(itmAtr[0]=="rPercentTimeDeadModPerLevel"):
                print(-99);
"""

"""
Summoners:
    20250099 - MonsterMashU2
    68281280 - ursinfulnature
    68592030 - serpentacus
    47584599 - rainbow dashOP
    
"""
summonerID = 47584599

"""   MATCH HISTORY
partUrl = "https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/" + str(summonerID) + "?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(partUrl)
matchlist = response.json()
print(matchlist)

recMatchID = matchlist['matches'][0]['matchId']

matchUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/"+str(recMatchID)+"?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(matchUrl)
matchdata = response.json()

participants = matchdata['participantIdentities']
"""

"""   CURRENT MATCH
"""

currUrl = "https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/"+str(summonerID)+"?api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(currUrl)
matchdata = response.json()

participants = matchdata['participants']
participantID = 0
for i in range(0, len(participants)):
    """ MATCH HISTORY
    if participants[i]['player']['summonerId'] == summonerID:
        participantID = i
    """
    
    """ CURRENT MATCH
    """
    
    if participants[i]['summonerId'] == summonerID:
        participantID = i

playerInfo = matchdata['participants'][participantID]
championID = playerInfo['championId']
champUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(championID)+"?champData=info&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
response = requests.get(champUrl)
allDatas = response.json()
champName = allDatas['name']
print("Playing: " + champName)
print()

mastery = playerInfo['masteries']
print("Masteries:")
for i in range(0, len(mastery)):
    mStat = mastery[i]
    points = mStat['rank']
    masID = mStat['masteryId']
    mastUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/mastery/"+str(masID)+"?masteryData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(mastUrl)
    allDatas = response.json()
    name = allDatas['name']
    descript = allDatas['description'][points-1]
    print(name + ": " + descript)

runes = playerInfo['runes']
print()
print("Runes:")
for i in range(0, len(runes)):
    rStat = runes[i]
    number = rStat['count']
    runeID = rStat['runeId']
    runeUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/rune/"+str(runeID)+"?runeData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(runeUrl)
    allRune = response.json()
    descript = allRune['description']
    print("x" + str(number)+": " + str(descript))