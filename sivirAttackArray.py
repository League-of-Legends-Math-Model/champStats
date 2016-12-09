# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:53:55 2016

@author: JK Rutter
"""

import numpy as np
import random as rng

sivirAbSequence = [1, 2, 1, 3, 1, 4, 1, 2, 1, 2, 4, 2, 2, 3, 3, 4, 3, 3]

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
    id == 3087 or #static shiv
    id == 3508    #ess reav
"""
totalSteps = 15
rapidfirecannon = np.array([50, 50, 50, 50, 50, 58, 66, 75, 83, 92, 100, 109, 117, 126, 134, 143, 151, 160])
statikkshiv = np.array([50, 50, 50, 50, 50, 56, 61, 67, 72, 77, 83, 88, 94, 99, 104, 110, 115, 120])

def sivirAttackArray(statMatr, itemArray):
    #NEW SEQUENCE
    genDamage = [0, 0, 0]
    genResist = [0, 0, 0, 0, 0, 0, 0, 0]

    sequence = []

    for i in range(0, totalSteps):
        sequence.append([0, genDamage, genResist, 0])
    #NEW SEQUENCE
    
    sivirUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/15?champData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
    response = requests.get(sivirUrl)
    sivir = response.json()
    baseStats = sivir['stats']
    spells = sivir['spells']
    attackDelay = 0.625 / (1 + baseStats['attackspeedoffset'])
    baseAD = baseStats['attackdamage'] + baseStats['attackdamageperlevel'] * (statMatr[8] - 1) * (0.685 + 0.0175 * statMatr[8])
    itemEffectBank = [
    [1018, 0, 0, 0, 0, 0, 0, 0, 0],
    [1027, 0, 0, 0, 0, 0, 0, 0, 0],
    [1028, 0, 0, 0, 0, 0, 0, 0, 0],
    [1036, 0, 0, 0, 0, 0, 0, 0, 0],
    [1037, 0, 0, 0, 0, 0, 0, 0, 0],
    [1038, 0, 0, 0, 0, 0, 0, 0, 0],
    [1042, 0, 0, 0, 0, 0, 0, 0, 0],
    [1043, 0, 0, 0, 0, 0, 0, 0, 0],
    [1051, 0, 0, 0, 0, 0, 0, 0, 0],
    [1053, 0, 0, 0, 0, 0, 0, 0, 0],
    [2015, 0, 0, 0, 0, 40, 0, 0, 0],
    [3101, 0, 0, 0, 0, 0, 0, 0, 0],
    [3133, 0, 0, 0, 0, 0, 0, 0, 0],
    [3031, .5, 0, 0, 0, 0, 0, 0, 0],
    [3034, 0, 0, 0, .1, 0, 0, 0, 0],
    [3035, 0, 0, 0, 0, 0, 0, 0, 0],
    [3035, 0, 0, 0, .15, 0, 0, 0, 0],
    [3044, 0, 0, 0, 0, 0, 0, 0, 0],
    [3046, 0, 0, 0, 0, 0, 0, 0, 0],
    [3057, 0, baseAD, 0, 0, 0, 0, 0, 0],
    [3072, 0, 0, 0, 0, 0, 0, 0, 0],
    [3078, 0, 2*baseAD, 0, 0, 0, 0, 0, 0],
    [3085, 0, 0, 15, 0, 0, 0, 0, 0],
    [3086, 0, 0, 0, 0, 0, 0, 0, 0],
    [3094, 0, 0, 0, 0, rapidfirecannon[statMatr[8]], 0, 0, 0],    
    [3087, 0, 0, 0, 0, statikkshiv[statMatr[8]], 0, 0, 0],
    [3508, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # if infinity edge, critDamage = 2.5    
    critDamage = 2    
    oneShotPhyEnhance = 0
    regPhyOnHit = 0
    phyEnhance = 1
    oneShotMagEnhance = 0
    regMagOnHit = 0
    lethality = 0
    perArmorPen = 0
    
    for i in range(0, len(itemArray)):
        for j in range(0, 27):
            if itemArray[i] == itemEffectBank[j][0]:
                critDamage = critDamage + itemEffectBank[j][1]
                oneShotPhyEnhance = oneShotPhyEnhance + itemEffectBank[j][2]
                regPhyOnHit = regPhyOnHit + itemEffectBank[j][3]
                phyEnhance = phyEnhance + itemEffectBank[j][4]
                oneShotMagEnhance = oneShotMagEnhance + itemEffectBank[j][5]
                regMagOnHit = regMagOnHit + itemEffectBank[j][6]
                lethality = lethality + itemEffectBank[j][7]
                if itemEffectBank[j][8] > 0 and perArmorPen > 0:
                    perArmorPen = perArmorPen * itemEffectBank[j][8]
                elif itemEffectBank[j][8] > 0:
                    perArmorPen = itemEffectBank[j][8]
    
    abilityPoints = [0, 0, 0, 0]
    
    for i in range(0, int(statMatr[8])):
        abilityPoints[sivirAbSequence[i]-1] = abilityPoints[sivirAbSequence[i]-1] + 1
    
    onePassBlade = spells[0]['effect'][1][abilityPoints[0] - 1] + spells[0]['effect'][4][abilityPoints[0] - 1] * statMatr[4]

    boomerangBlade = onePassBlade + onePassBlade * (1 - spells[0]['effect'][2][abilityPoints[0] - 1] / 100)

    ricochet = 0
    
    if abilityPoints[3] > 0:
        ricochet = (spells[3]['effect'][1][abilityPoints[3] - 1]) / 100
        
    for i in range(0, totalSteps):
        sequence[i][0] = 1 / statMatr[5]
    
    #Armor Penetration Modifiers
    for i in range(0, totalSteps):
        sequence[i][2] = [0, 0, perArmorPen, lethality, 0, 0, 0, 0]
    
    #Attack Types
    for i in range(0, totalSteps):
        sequence[i][3] = 0    
    
    critted = rng.random()
    
    #first ability
    sequence[0][0] = 0
    sequence[0][1] = [boomerangBlade * phyEnhance, 0, 0]
    sequence[0][3] = 1
    
    #ricochet attacks
    for i in range(1, 4):        
        sequence[i][0] = 1 / (statMatr[5] + attackDelay * ricochet)
    
    sequence[1][1] = [(statMatr[4] + regPhyOnHit + oneShotPhyEnhance) * phyEnhance, oneShotMagEnhance + regMagOnHit, 0]
    
    if critted <= statMatr[6]:
        sequence[1][1][0] = (statMatr[4] * critDamage + regPhyOnHit + oneShotPhyEnhance) * phyEnhance
    
    for i in range(2, totalSteps):
        critted = rng.random()
        sequence[i][1] = [(statMatr[4] + regPhyOnHit) * phyEnhance, regMagOnHit, 0]
        if critted <= statMatr[6]:
            sequence[i][1][0] = (statMatr[4] * critDamage + regPhyOnHit) * phyEnhance
    
    # other item changes
    return sequence