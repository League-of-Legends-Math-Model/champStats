# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:52:34 2016

@author: JK Rutter

Thinking about it, we might only need to compute 9 rotations.  At that point,
it will probably recycle.
"""

import numpy as np
import random as rng

caitAbSequence = [2, 1, 3, 2, 2, 4, 2, 1, 2, 1, 4, 1, 1, 3, 3, 4, 3, 3]

"""
    statMatr
    0 - Health
    1 - Health Regen
    2 - Armor
    3 - Magic Resist
    4 - Attack Damage
    5 - Attack Speed
    6 - Critical Strike %
    7 - Life Steal %
    8 - Level
"""

"""
ITEM BANK
    id == 1018 or # cloak of agility
    id == 1027 or # saphire crystal
    id == 1028 or  #ruby crystal
    id == 1036 or  #long sword
    id == 1037 or    #pickaxe
    id == 1038 or     # b.f. sword
    id == 1042 or ##dagger
    id == 1043 or     #recursive bow
    id == 1051 or ## brawlers gloves
    id == 1053 or #vampire scepter
    id == 2015 or #kshard
    id == 3101 or    # stinger
    id == 3133 or  #caulefield warhammer
    id == 3031 or #infinty edge
    id == 3034 or   #giant slayer
    id == 3035 or   #last whisper
    id == 3036 or  #Lord D regards
    id == 3044 or  #phage
    id == 3046 or  #phantom dancer
    id == 3057 or  ##sheen
    id == 3072 or #the blood thirstie
    id == 3078 or #trinty force
    id == 3085 or #runnans hurricaine
    id == 3086 or # recursive bow
    id == 3094 or #rapid fire cannn
    id == 3086 or #static shiv
    id == 3508    #ess reav
"""
totalSteps = 15
rapidfirecannon = np.array([50, 50, 50, 50, 50, 58, 66, 75, 83, 92, 100, 109, 117, 126, 134, 143, 151, 160])
statikkshiv = np.array([50, 50, 50, 50, 50, 56, 61, 67, 72, 77, 83, 88, 94, 99, 104, 110, 115, 120])

def caitAttackArray(statMatr, itemArray):
    sequence = np.zeros(shape=(2, totalSteps))
    
    caitUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/51?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(caitUrl)
    cait = response.json()
    baseStats = cait['stats']
    spells = cait['spells']
    
    baseAD = baseStats['attackdamage'] + baseStats['attackdamageperlevel'] * (statMatr[8] - 1) * (0.685 + 0.0175 * statMatr[8])
    itemEffectBank = [
    [1018, 0, 0, 0, 0],
    [1027, 0, 0, 0, 0],
    [1028, 0, 0, 0, 0],
    [1036, 0, 0, 0, 0],
    [1037, 0, 0, 0, 0],
    [1038, 0, 0, 0, 0],
    [1042, 0, 0, 0, 0],
    [1043, 0, 0, 0, 0],
    [1051, 0, 0, 0, 0],
    [1053, 0, 0, 0, 0],
    [2015, 0, 40, 0, 0],
    [3101, 0, 0, 0, 0],
    [3133, 0, 0, 0, 0],
    [3031, .5, 0, 0, 0],
    [3034, 0, 0, 0, .1],
    [3035, 0, 0, 0, 0],
    [3035, 0, 0, 0, .15],
    [3044, 0, 0, 0, 0],
    [3046, 0, 0, 0, 0],
    [3057, 0, baseAD, 0, 0],
    [3072, 0, 0, 0, 0],
    [3078, 0, 2*baseAD, 0, 0],
    [3085, 0, 0, 15, 0],
    [3086, 0, 0, 0, 0],
    [3094, 0, rapidfirecannon[statMatr[8]], 0, 0],    
    [3096, 0, statikkshiv[statMatr[8]], 0, 0],
    [3508, 0, 0, 0, 0]
    ]
    # if infinity edge, critDamage = 2.5    
    critDamage = 2    
    oneShotEnhance = 0
    regOnHit = 0
    phyEnhance = 1
    
    for i in range(0, 5):
        for j in range(0, 27):
            if itemArray[i] == itemEffectBank[j][0]:
                critDamage = critDamage + itemEffectBank[j][1]
                oneShotEnhance = oneShotEnhance + itemEffectBank[j][2]
                regOnHit = regOnHit + itemEffectBank[j][3]
                phyEnhance = phyEnhance + itemEffectBank[j][4]
    
    abilityPoints = [0, 0, 0, 0]
    
    for i in range(0, statMatr[8]):
        abilityPoints[caitAbSequence[i]-1] = abilityPoints[caitAbSequence[i]-1] + 1
    #headshot and multipliers don't show up anywhere in the API
    headshot = statMatr[4] + (.5 + .5 * critDamage * statMatr[6])*statMatr[4]
    critHeadshot = headshot + statMatr[4] * (critDamage - 1)
    #the .7 multiplier from trapHeadshot doesn't show up anywhere in the API
    trapHeadshot = headshot + spells[1]['effect'][1][abilityPoints[1]] + .7 * statMatr[4]    
    trapCritHS = trapHeadshot + statMatr[4] * (critDamage - 1)
    caliberNet = spells[2]['effect'][1][abilityPoints[2]]
    peacemaker = spells[0]['effect'][1][abilityPoints[0]] + (spells[0]['effect'][5][abilityPoints[0]]) * statMatr[4]
    
    for i in range(0, 15):
        sequence[0][i] = 1 / statMatr[5]
    
    critted = rng.random()
    
    sequence[1][0] = (trapHeadshot + oneShotEnhance + regOnHit)*phyEnhance
    
    if critted <= statMatr[6]:
        sequence[1][0] = (trapCritHS + oneShotEnhance + regOnHit)*phyEnhance
    
    sequence[0][1] = 0.25
    sequence[1][1] = caliberNet
    
    sequence[1][2] = (headshot + regOnHit)*phyEnhance
    
    critted = rng.random()
    
    if critted <= statMatr[6]:
        sequence[1][2] = (critHeadshot + regOnHit)*phyEnhance
    
    critted = rng.random()
    sequence[1][3] = (headshot + regOnHit)*phyEnhance
    if critted <= statMatr[6]:
        sequence[1][3] = (critHeadshot + regOnHit)*phyEnhance
    
    for i in range(4, totalSteps):
        critted = rng.random()
        sequence[1][i] = (statMatr[4] + regOnHit)*phyEnhance
        if critted <= statMatr[6]:
            sequence[1][i] = (statMatr[4] * critDamage + regOnHit)*phyEnhance
    if totalSteps > 10:
        critted = rng.random()
        sequence[1][10] = (headshot + regOnHit)*phyEnhance
        if critted <= statMatr[6]:
            sequence[1][10] = (critHeadshot + regOnHit)*phyEnhance
        
    # other item changes
    
    return sequence

def calcDPS(caitSeq):
    time = 0
    damage = 0    
    for i in range(0, totalSteps):
        time = time + caitSeq[0][i]
        damage = damage + caitSeq[1][i]
    return damage / time