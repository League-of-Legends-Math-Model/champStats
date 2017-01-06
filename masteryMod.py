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
    32 - ALL DAMAGE INCREASE
    33 - ALL DAMAGE REDUCTION
    
    
FLOW DIAGRAM
(X) = COMPLETED
1: BUILD CHARACTER
2: BUILD CHARACTER TO LEVEL
X: PREMOD
4: FLAT RUNES
5: LEVEL RUNES
X: PRELEVELMOD
7: ITEMS (AND FLAT MOVEMENT SPEED ITEMS, NOT PERCENTAGE MOVEMENT SPEED)
X: MOVEMENT
9: ITEMS -- PERCENTAGE MOVEMENT SPEED
X: POSTMOD
X: ENEMYMOD
X: DAMAGEMORPH
X: UNIQUES
X: ONHITS
X: HEALSHIELD
X: WARNINGS
17: CALCULATE ABILITY AND AUTO DAMAGE

RETURNS

X: PREMOD        | statarray
X: PRELEVELMOD   | statarray
X: MOVEMENT      | statarray
X: POSTMOD       | statarray
X: ENEMYMOD      | statarray
X: DAMAGEMORPH   | damageoutput [all damage, ability damage, damage reduction]
X: UNIQUES       | returnValue [summoner CDR, colossus shield, colossus CD]
X: ONHITS        | onHitInfo 2d [[damage info], CD]
X: HEALSHIELD    | hsEnhance (multiplier for shields/healing)
X: WARNINGS      | problems array [list of warnings]
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
[6242, 0, .5, 0],
[6222, 15, 8, 0],
[6222, 17, 8, 0],
[6161, 30, .2, 0],
[6251, 27, 0, .03],
[6251, 28, 0, .03]
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
[6154, 26, .014, 0, 0],  #percent
[6231, 2, .016, 0, 0],
[6231, 30, .016, 0, 0]
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
[masteryId, damage type (0 = phy, 1 = mag, 2 = true), base, level bonus, base ad bonus, ap bonus, max health, enemy curr health, baseCD, levelmod, bonus AD]
6121 FIRST BLOOD
6261 GRASP OF THE UNDYING
6341 GREENFATHER'S GIFT
6362 THUNDERLORD'S DECREE
6162 FERVOR OF BATTLE (treated at max stacks)
6164 DEATHFIRE TOUCH
"""

onHits = [
[6121, 2, 10, 1, 0, 0, 0, 0, 6, 0, 0],
[6261, 1, 0, 0, 0, 0, .03, 0, 4, 0, 0],
[6341, 1, 0, 0, 0, 0, 0, .03, 9, 0, 0],
[6362, 1, 0, 10, .3, .1, 0, 0, 25.588, .588, 0],
[6162, 0, 4.72, 3.28, 0, 0, 0, 0, 0, 0, 0],
[6164, 1, 8, 0, 0, .25, 0, 0, 0, 0, .6]
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
[6242, "This unit gains triple hp regen when under 25% health."],
[6363, "This unit's shields and heals are more powerful and give armor and MR."]
]

#damageMorph = [mastery ID, auto increase, ability increase, damage reduction] all by points

damageMorph = [
[6141, 1.075, 1.075, 1],
[6142, 1.05, 1.05, 1.025],
[6143, 1.05, 1.05, 1],
[6323, 1.02, 1.02, 1],
[6263, 1, 1, .96],
[6114, 1, 1.004, 1],
[6331, 1.01, 1.01, 1]
]

#movement = [mastery ID, base increase, percentage increase] all by points

movement = [
[6221, 15, 1],
[6311, 0, 1.006]
]

#healShield = [mastery ID, % increase, % increase points]
healShield = [
[6363, 1.1, 0],
[6231, 1, .016]
]

"""
UNIQUES -
6241 - INSIGHT
6262 - COURAGE OF THE COLOSSUS
"""
#uniques = [mastery ID, % summoner spell cdr, base shield, level mult, max health, CD base, CDR level]
uniques = [
[6241, .25, 0, 0, 0, 0, 9],
[6262, 0, 10, 10, .25, 45.88, .88]
]

#CALCULATE FOR SUMMONER SPELL CD AND PASS IN CASE OF COURAGE, AFTER EVERYTHING
def uniqueStats(masteryArray, baseStatArray, level):
    returnValue = [1, 0, 0]
    for j in range(0, len(masteryArray)):
        if masteryArray[j]['masteryId'] == 6241:
            returnValue[0] = returnValue[0] - uniques[0][1]
        if masteryArray[j]['masteryId'] == 6262:
            returnValue[1] = uniques[1][2] + uniques[1][3] * level
            returnValue[2] = uniques[1][4] - uniques[1][5] * level
    return returnValue

#CALCULATE FOR A HEALING OR A SHIELD ABILITY
def healShieldStat(masteryArray):
    hsEnhance = 1
    for i in range(0, len(healShield)):
        for j in range(0, len(masteryArray)):
            if masteryArray[j]['masteryId'] == healShield[i][0]:
                hsEnhance = (hsEnhance * healShield[i][1])*(1 + healShield[i][2] * masteryArray[j]['rank'])
    return hsEnhance

#AFTER FLAT MOVEMENT SPEED ITEMS, BEFORE PERCENTAGE MOVEMENT SPEED ITEMS
def moveStats(masteryArray, baseStatArray):
    for i in range(0, len(movement)):
        for j in range(0, len(masteryArray)):
            if masteryArray[j]['masteryId'] == movement[i][0]:
                baseStatArray[19] = (baseStatArray[19] + movement[i][1]) * movement[i][2]
    return baseStatArray

#AFTER EVERYTHING
def warningStats(masteryArray):
    problems = []
    for i in range(0, len(masteryArray)):
        for j in range(0, len(warnings)):
            if masteryArray[i]['masteryId'] == warnings[j][0]:
                problems.append(warnings[j][1])
    return problems

#AFTER ALL ITEMS, BEFORE CALCULATION
def damageMorphStats(masteryArray):
    damageOutput = [1, 1, 1]
    for i in range(0, len(masteryArray)):
        for j in range(0, len(damageMorph)):
            if masteryArray[i]['masteryId'] == warnings[j][0]:
                for k in range(0, 3):
                    damageOutput[k] = damageOutput[k] * damageMorph[j][k + 1] * masteryArray[i]['rank']
    return damageOutput

#BEFORE ITEMS
def preModStats(masteryArray, baseStatArray):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(preMod)):
            if masteryArray[i]['masteryId'] == preMod[j][0]:
                baseStatArray[preMod[j][1]] = baseStatArray[preMod[j][1]] + baseStatArray[preMod[j][1]]*preMod[j][2] + preMod[j][3] * masteryArray[i]['rank']
    return baseStatArray

#BEFORE ITEMS
def preLevelModStats(masteryArray, baseStatArray, level):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(preLevelMod)):
            if masteryArray[i]['masteryId'] == preLevelMod[j][0]:
                baseStatArray[preLevelMod[j][1]] = baseStatArray[preLevelMod[j][1]] + preLevelMod[j][2] + preLevelMod[j][3] * masteryArray[i]['rank'] + preLevelMod[j][4] * masteryArray[i]['rank'] * level
    return baseStatArray

#AFTER ITEMS
def postModStats(masteryArray, baseStatArray, champBaseAtLevel):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(postMod)):
            if masteryArray[i]['masteryId'] == postMod[j][0]:
                baseStatArray[postMod[j][1]] = baseStatArray[postMod[j][1]] * (1 + postMod[j][2] * masteryArray[i]['rank']) + champBaseAtLevel[postMod[j][1]] * postMod[j][4] * masteryArray[i]['rank'] + (baseStatArray[postMod[j][1]] - champBaseAtLevel[postMod[j][1]]) * postMod[j][3] * masteryArray[i]['rank']
    return baseStatArray

#AFTER ITEMS
def enemyModStats(masteryArray, baseStatArray, level, enemies):
    for i in range(0, len(masteryArray)):
        for j in range(0, len(enemyMod)):
            if masteryArray[i]['masteryId'] == enemyMod[j][0]:
                baseStatArray[enemyMod[j][1]] = baseStatArray[enemyMod[j][1]] * (1 + enemyMod[j][2]) + enemyMod[j][3] * masteryArray[i]['rank'] * enemyMod[j][5] * enemies + enemyMod[j][4] * level * (1 - enemyMod[j][5])
    return baseStatArray            

#AFTER EVERYTHING
def masteryOnHits(masteryArray, baseStatArray, enemyStatArray, level, champBaseAtLevel):
    onHitsInfo = []
    for i in range(0, len(masteryArray)):
        for j in range(0, len(onHits)):
            if masteryArray[i]['masteryId'] == onHits[j][0]:
                damage = onHits[j][2] + onHits[j][3] * level + onHits[j][4] * champBaseAtLevel[8] + onHits[j][5] * baseStatArray[20] + onHits[j][6] * baseStatArray[0] + onHits[j][7] * enemyStatArray[0] + onHits[j][10] * (baseStatArray[8] - champBaseAtLevel[8])
                damageArray = [0, 0, 0]
                damageArray[onHits[j][1]] = damage
                cooldown = onHits[j][8] - onHits[j][9] * level
                onHitsInfo.append([damageArray, cooldown])
    return onHitsInfo