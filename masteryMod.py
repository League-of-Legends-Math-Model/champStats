# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 07:53:55 2016

@author: Jon-Michael

Mastery Stat Modifier

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
"""
#preMod = [mastery ID, stat #, base stat % increase, stack / point]
preMod = [
[6352, 29, 0, .01],
[6351, 22, 0, 1.7],
[6211, 2, 0, .4],
[6111, 14, 0, .008],
[6131, 30, 0, .004],
[6131, 31, 0, .004],
[6232, 0, 0, 10],
[6242, 0, .5, 0]
]

#preLevelMod = [mastery ID, stat #, base, stack / point, points * level]
preLevelMod = [
[6351, 25, 0, .6, .06],
[6134, 8, 0, .4, .091],
[6134, 20, 0, .6, .133]
]

#postMod = [mastery ID, stat #, total % / point, bonus % / point, base % / point]
postMod = [
[6212, 15, 0, .01, 0],  #percent
[6212, 17, 0, .01, 0],  #percent
[6151, 22, .014, 0, 0], #percent
[6151, 23, .014, 0, 0], #percent
[6151, 24, .014, 0, 0], #percent
[6154, 25, .014, 0, 0], #percent
[6154, 26, .014, 0, 0]  #percent
]

#enemyMod = [mastery ID, stat #, % increase, flat increase points, flat level increase, proximity matters]
enemyMod = [
[6243, 15, 0.1, 0, 2, 0],
[6243, 17, 0.1, 0, 2, 0],
[6252, 15, 0, .6, 0, 1],
[6252, 17, 0, .6, 0, 1]
]

#onHits (extra on hit damage from masteries)
"""ON HITS
[masteryId, damage type (0 = phy, 1 = mag, 2 = true), base, level bonus, base ad bonus, ap bonus, max health, enemy curr health, baseCD, levelmod]
6121 FIRST BLOOD
6261 GRASP OF THE UNDYING
6341 GREENFATHER'S GIFT
6362 THUNDERLORD'S DECREE
"""

onHits = [
[6121, 2, 10, 1, 0, 0, 0, 0, 6, 0],
[6261, 1, 0, 0, 0, 0, .03, 0, 4, 0],
[6341, 1, 0, 0, 0, 0, 0, .03, 9, 0],
[6362, 1, 0, 10, .3, .1, 0, 0, 25.588, .588]
]
#warnings = [mastery ID, text]
warnings = [
[6123, "When this unit damages you, their allies will do 3% more damage to you."],
[6141, "This unit does more damage based on the unique kills they have."],
[6321, "This unit has buffs for 15% longer (blue buff/red buff last 2:18)."],
[6263, "This unit will take 6% of surrounding allies' damage down to 5% health."],
[6343, "This unit recovers 5% of their missing health and mana upon killing an enemy champion."],
[6332, "This unit passive recovers missing mana."],
[6252, "This unit gains extra armor and magic resist based on the number of nearby enemies."],
[6361, "This unit gains increased movement speed (40%, equivalent to a level 13 Ghost) and 75% slow resist."]
]


def preModStats(masteryArray, baseStatArray):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(preMod)):
            if masteryArray[i]['masteryId'] == preMod[j][0]:
                baseStatArray[preMod[j][1]] = baseStatArray[preMod[j][1]] + baseStatArray[preMod[j][1]]*preMod[j][2] + preMod[j][3] * masteryArray[i]['rank']
    return baseStatArray

def preLevelModStats(masteryArray, baseStatArray, level):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(preLevelMod)):
            if masteryArray[i]['masteryId'] == preLevelMod[j][0]:
                baseStatArray[preLevelMod[j][1]] = baseStatArray[preLevelMod[j][1]] + preLevelMod[j][2] + preLevelMod[j][3] * masteryArray[i]['rank'] + preLevelMod[j][4] * masteryArray[i]['rank'] * level
    return baseStatArray

def postModStats(masteryArray, baseStatArray, champBaseAtLevel):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(postMod)):
            if masteryArray[i]['masteryId'] == postMod[j][0]:
                baseStatArray[postMod[j][1]] = baseStatArray[postMod[j][1]] * (1 + postMod[j][2] * masteryArray[i]['rank']) + champBaseAtLevel[postMod[j][1]] * postMod[j][4] * masteryArray[i]['rank'] + (baseStatArray[postMod[j][1]] - champBaseAtLevel[postMod[j][1]]) * postMod[j][3] * masteryArray[i]['rank']
    return baseStatArray

def enemyModStats(masteryArray, baseStatArray, level, enemies):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(enemyMod)):
            if masteryArray[i]['masteryId'] == enemyMod[j][0]:
                baseStatArray[enemyMod[j][1]] = baseStatArray[enemyMod[j][1]] * (1 + enemyMod[j][2]) + enemyMod[j][3] * masteryArray[i]['rank'] * enemyMod[j][5] * enemies + enemyMod[j][4] * level * (1 - enemyMod[j][5])
    return baseStatArray            

def masteryOnHits(masteryArray, baseStatArray, enemyStatArray, level, champBaseAtLevel):
    onHitsInfo = []
    for i in range(0, len(masteryArray)):
        for j in range(0, len(onHits)):
            if masteryArray[i]['masteryId'] == onHits[j][0]:
                damage = onHits[j][2] + onHits[j][3] * level + onHits[j][4] * champBaseAtLevel[8] + onHits[j][5] * baseStatArray[20] + onHits[j][6] * baseStatArray[0] + onHits[j][7] * enemyStatArray[0]
                damageArray = [0, 0, 0]
                damageArray[onHits[j][1]] = damage
                cooldown = onHits[j][8] - onHits[j][9] * level
                onHitsInfo.append([damageArray, cooldown])
    return onHitsInfo