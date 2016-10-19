# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:25:46 2016

@author: JK Rutter
"""



import math
import numpy as np

sivirLevel = 18
quinnLevel = 18
rapidfirecannon = np.array([50, 50, 50, 50, 50, 58, 66, 75, 83, 92, 100, 109, 117, 126, 134, 143, 151, 160])


def Quinn():
    return np.array([[532.8, 5.42, 54.46, 0.668, 23.38, 30,0,0,0],[85, 0.55, 2.41, .031, 3.5, 0,0,0,0]]) 

def Sivir():
    return np.array([[515.76, 5.17, 57.46, 0.625, 22.21, 30,0,0,0],[82, 0.55, 2.41, .016, 3.25, 0,0,0,0]])

def growth(charBase, charGrowth, level):
    return charBase + charGrowth * (level - 1) * (0.685 + 0.0175 * level)
    
def BoomerangBlade(points):
    possDamage = [(46.25 + 37 * (points-1)), (129.5 + 18.5 * (points - 1))]
    return possDamage

def Ricochet(points):
    return .30 + .15 * (points - 1)

def BlindingAssault(points):
    possDamage = [(20 + 25 * (points - 1)), (80 + 10 * (points - 1))]
    return possDamage

def HeightenedSenses(points):
    return .2 + .5 * (points - 1)

def Vault(points):
    possDamage = [(40 + 30* (points - 1)), .2]
    return possDamage

"""
Add Items Here
"""

def SivirItems(itemIndex):
    itemArray = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, 6):
        itemIndexMod(itemIndex[i],itemArray, sivirLevel)
    return itemArray

def QuinnItems(itemIndex):
    itemArray = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, 6):
        itemIndexMod(itemIndex[i],itemArray, quinnLevel)
    return itemArray

def itemIndexMod(itemNum, currAug, charLevel):
    """
    ITEM INDEX NUMBERS
    1 = Essence Reaver
    2 = Infinity Edge
    3 = The Bloodthirster
    4 = Mercurial Scimitar
    5 = Berserker's Greaves
    6 = Rapid Firecannon
    """
    if itemNum == 1:
        currAug[2] = currAug[2] + 70
        currAug[7] = currAug[7] + .2
    elif itemNum == 2:
        currAug[2] = currAug[2] + 70
        currAug[7] = currAug[7] + .2
    elif itemNum == 3:
        currAug[2] = currAug[2] + 75
        currAug[6] = currAug[6] + .2
        if charLevel > 16:
            currAug[0] = currAug[0] + 40 + charLevel * 10 + (charLevel - 6) * 10 + (charLevel - 16) * 5
        elif sivirLevel > 6:
            currAug[0] = currAug[0] + 40 + charLevel * 10 + (charLevel - 6) * 10
        else:
            currAug[0] = currAug[0] + 40 + charLevel * 10
    elif itemNum == 4:
        currAug[2] = currAug[2] + 65
        currAug[5] = currAug[5] + 35
        currAug[6] = currAug[6] + .1
    elif itemNum == 5:
        currAug[3] = currAug[3] + .35
    elif itemNum == 6:
        currAug[3] = currAug[3] + .3
        currAug[7] = currAug[7] + .3
    return currAug
"""
Generate attack array
"""


def genSivirAttackArray(stats, items, boomblade, bounce):
    results = np.zeros(shape=(2, 15))
    results[0][0] = 0
    results[1][0] = boomblade[0] + boomblade[1] * (growth(stats[0][2], stats[1][2], sivirLevel)+items[2])
    for i in range(1, 4):
        results[0][i] = 1 / (stats[0][3] + stats[0][3] * (growth(0, stats[1][3],sivirLevel)+items[3] + bounce))
    for i in range(4, 15):
        results[0][i] = 1 / (stats[0][3] + stats[0][3] * (growth(0, stats[1][3],sivirLevel)+items[3]))
    for i in range(1, 15):
        results[1][i] = growth(stats[0][2], stats[1][2], sivirLevel) + items[2]
    """
    On Hits
    
    Rapid Firecannon, which acts as magic damage (potentially AD/MD/TD components in the future?)
    """
    results[1][1] = results[1][1] + rapidfirecannon[sivirLevel - 1]
    return results
    
def genQuinnAttackArray(stats, items, blind, sense, jump):
    results = np.zeros(shape=(2, 15))
    """
    Begins with Skystrike, her ult with a time frame 0.
    """    
    results[0][0] = 0
    results[1][0] = growth(stats[0][2], stats[1][2], quinnLevel) + items[2]
    results[0][1] = 0.25
    results[1][1] = jump[0] + jump[1] * (growth(stats[0][2], stats[1][2], quinnLevel) + items[2])
    results[0][2] = 1 / (stats[0][3] + stats[0][3] * (growth(0, stats[1][3],quinnLevel)+items[3]))
    results[1][2] = 10 + 5 * quinnLevel + (.14 + .02 * quinnLevel) * (growth(stats[0][2], stats[1][2], quinnLevel) + items[2]) + growth(stats[0][2], stats[1][2], quinnLevel) + items[2]
    results[0][3] = 0
    results[1][3] = blind[0] + blind[1] * (growth(stats[0][2], stats[1][2], quinnLevel) + items[2])
    results[0][4] = 1 / (stats[0][3] + stats[0][3] * (growth(0, stats[1][3],quinnLevel)+items[3]))
    results[1][4] = 10 + 5 * quinnLevel + (.14 + .02 * quinnLevel) * (growth(stats[0][2], stats[1][2], quinnLevel) + items[2]) + growth(stats[0][2], stats[1][2], quinnLevel) + items[2]
    for i in range(5, 8):
        results[0][i] = 1 / (stats[0][3] + stats[0][3] * (growth(0, stats[1][3],quinnLevel)+items[3]+sense))
    for i in range(8, 15):
        results[0][i] = 1 / (stats[0][3] + stats[0][3] * (growth(0, stats[1][3],quinnLevel)+items[3]))
    for i in range(5, 15):
        results[1][i] = growth(stats[0][2], stats[1][2], quinnLevel) + items[2]
    return results

sivirDamage = genSivirAttackArray(Sivir(), SivirItems([1, 2, 3, 4, 5, 6]), BoomerangBlade(5), Ricochet(3))
quinnDamage = genQuinnAttackArray(Quinn(), QuinnItems([1, 2, 3, 4, 5, 6]), BlindingAssault(5), HeightenedSenses(5), Vault(5))

print(sivirDamage)
print(quinnDamage)
sivirTime = 0
sivirDmg = 0
quinnTime = 0
quinnDmg = 0

for i in range(0, 15):    
    sivirTime = sivirTime + sivirDamage[0][i]
    sivirDmg = sivirDmg + sivirDamage[1][i]
    quinnTime = quinnTime + quinnDamage[0][i]
    quinnDmg = quinnDmg + quinnDamage[1][i]

print("Sivir Time: " + str(round(sivirTime)))
print("Sivir Damage: " + str(round(sivirDmg)))
print("Quinn Time: " + str(round(quinnTime)))
print("Quinn Damage: " + str(round(quinnDmg)))
print("Sivir DPS: " + str(round(sivirDmg/sivirTime)))
print("Quinn DPS: " + str(round(quinnDmg/quinnTime)))

def takeTurn(move,target, moveChampStats, targetChampStats):
#is a physical attack
    if (True):
        return (target - (move*(100/(100+targetChampStats[4]))));   #factor in armor etc
        

def battleDamadge(champ1BattleMatrix, champ2BattleMatrix,  champ1Stats, champ2Stats):


#name arrays
    Champ1MoveArray=champ1BattleMatrix[1];
    Champ1TimeStampArray=champ1BattleMatrix[0];
    Champ2MoveArray=champ2BattleMatrix[1];
    Champ2TimeStampArray=champ2BattleMatrix[0];
#Set Champions health    
    HealthChamp1 = champ1Stats[0];  #
    HealthChamp2 = champ2Stats[0];   #TBD
    
    timeBank1=0;
    timeBank2=0;
    index1=0;
    index2=0;
    for i in range(1,100):
        timeBank1 = timeBank1+1;
        timeBank2 = timeBank2+1;
        #if enough time has passed for champ1 to use move
        if(Champ1TimeStampArray[index1]<timeBank1):   # check if the move has been channeled long enough
            timeBank1=0;  # mark time as used
            HealthChamp2 = takeTurn(Champ1MoveArray[index1], HealthChamp2,champ1Stats, champ2Stats);
            index1 = index1 +1;
        #if enough time has passed for champ2 to use move
        if(Champ2TimeStampArray[index2]<timeBank2):
            timeBank2=0; 
            HealthChamp1 = takeTurn(Champ2MoveArray[index2], HealthChamp1,champ2Stats, champ1Stats);
            index2 = index2 +1;
            
        print(index1, index2, HealthChamp1, HealthChamp2);    
        #Check if either champ is dead        
        if(HealthChamp1 <= 0):
            print("champ1 dead");
            break;
        if(HealthChamp2 <= 0):
            print("champ2 dead");
            break;
            
champ1BattleMatrix = sivirDamage
champ2BattleMatrix = quinnDamage
statfun = Sivir()
champ1stats = growth(statfun[0],statfun[1],sivirLevel)+SivirItems([1, 2, 3, 4, 5, 6])
statfun2 = Quinn()
champ2stats = growth(statfun2[0],statfun[1],quinnLevel) + QuinnItems([1, 2, 3, 4, 5, 6])
print(champ1BattleMatrix[0]);
battleDamadge(champ1BattleMatrix, champ2BattleMatrix, champ1stats, champ2stats);
#battleDamadge(champ1Move, champ1time, champ2Move, champ2time);