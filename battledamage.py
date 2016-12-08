# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:53:30 2016

@author: JK Rutter
"""

#Combat Exchange

"""

reductions
[0] = flat armor reduction
[1] = percent armor reduction
[2] = percent armor penetration
[3] = lethality
[4] = flat mr reduction
[5] = percent mr reduction
[6] = percent mpenetration
[7] = flat mpenetration

damage
[0] = physical
[1] = magic
[2] = true
"""

def resultAttack(damage, reductions, attackerStats, defenderStats):
    defenderArmor = defenderStats[2]
    defenderArmor = defenderArmor - reductions[0]
    if defenderArmor > 0:
        defenderArmor = defenderArmor * (1 - reductions[1])
        defenderArmor = defenderArmor * (1 - reductions[2])
        defenderArmor = defenderArmor - reductions[3]*(.4 + defenderStats[8]/30)
    
    defenderResist = defenderStats[3]
    defenderResist = defenderResist - reductions[4]
    if defenderResist > 0:
        defenderResist = defenderResist * (1 - reductions[5])
        defenderResist = defenderResist * (1 - reductions[6])
        defenderResist = defenderResist - reductions[7]
    
    resultingArmor = 100 / (100 + defenderArmor)
    if defenderArmor < 0:
        resultingArmor = 2 - 100 / (100 - defenderArmor)
    
    resultingMR = 100 / (100 + defenderResist)
    if defenderResist < 0:
        resultingMR = 2 - 100 / (100 - defenderResist)
    
    phyDamage = damage[0] * resultingArmor
    magDamage = damage[1] * resultingMR
    truDamage = damage[2]
    
    actualDamage = [phyDamage, magDamage, truDamage]
    
    return actualDamage

def battleDamage(c1AttackArray, c2AttackArray, c1Stats, c2Stats):
    c1TimeStamps = []
    c1DamageStamps = []
    c1ResistStamps = []

    c2TimeStamps = []
    c2DamageStamps = []
    c2ResistStamps = []    
        
    for i in range(0, len(c1AttackArray)):    
        c1TimeStamps.append(c1AttackArray[i][0])
        c1DamageStamps.append(c1AttackArray[i][1])
        c1ResistStamps.append(c1AttackArray[i][2])  #Resistances
    
        c2TimeStamps.append(c2AttackArray[i][0])
        c2DamageStamps.append(c2AttackArray[i][1])
        c2ResistStamps.append(c2AttackArray[i][2]) #Resistances
    
    healthC1 = c1Stats[0]
    healthC2 = c2Stats[0]
    
    timeBank1 = 0
    timeBank2 = 0
    
    index1 = 0
    index2 = 0
    timeAt = 0
    active = True
    
    while(active):
        if index1 == len(c1TimeStamps):
            print("Champion 1 ran out of actions.")
            break;
        if index2 == len(c2TimeStamps):
            print("Champion 2 ran out of actions.")
            break;
        step1 = c1TimeStamps[index1]
        nextMove1 = timeBank1 + step1
        step2 = c2TimeStamps[index2]
        nextMove2 = timeBank2 + step2
        
        if nextMove1 < nextMove2:
            damageDone = resultAttack(c1DamageStamps[index1], c1ResistStamps[index1], c1Stats, c2Stats)
            healthLoss = 0
            for i in range(0, 3):
                healthLoss = healthLoss + damageDone[i]
            healthC2 = healthC2 - healthLoss
            
            #healthRegen - future check if grievious wounds
            healthC1 = healthC1 + (c1Stats[1] / 5) * (nextMove1 - timeAt)
            healthC2 = healthC2 + (c2Stats[1] / 5) * (nextMove1 - timeAt)
            
            #lifesteal - future check if grievious wounds, future check spell vamp
            if c1AttackArray[index1][3] == 0:
                healthC1 = healthC1 + c1Stats[7] * damageDone[0]
            
            # spell vamp

            # all damage health steal (death's dance)            
            
            index1 = index1 + 1
            timeAt = nextMove1
            
        if nextMove1 > nextMove2:
            damageDone = resultAttack(c2DamageStamps[index2], c2ResistStamps[index2], c2Stats, c1Stats)
            healthLoss = 0
            for i in range(0, 3):
                healthLoss = healthLoss + damageDone[i]
            healthC1 = healthC1 - healthLoss
            
            #healthRegen - future check if grievious wounds
            healthC1 = healthC1 + (c1Stats[1] / 5) * (nextMove1 - timeAt)
            healthC2 = healthC2 + (c2Stats[1] / 5) * (nextMove1 - timeAt)
            
            #lifesteal
            if c2AttackArray[index2][3] == 0:
                healthC2 = healthC2 + c2Stats[7] * damageDone[0]
            
            # other additions; spell vamp, all damage health steal            
            
            index2 = index2 + 1
            timeAt = nextMove2
        
        if nextMove1 == nextMove2:
            damageDone = resultAttack(c1DamageStamps[index1], c1ResistStamps[index1], c1Stats, c2Stats)
            healthLoss = 0
            for i in range(0, 3):
                healthLoss = healthLoss + damageDone[i]
            healthC2 = healthC2 - healthLoss
            
            if c1AttackArray[index1][3] == 0:
                healthC1 = healthC1 + c1Stats[7] * damageDone[0]
            
            damageDone = resultAttack(c2DamageStamps[index2], c2ResistStamps[index2], c2Stats, c1Stats)
            healthLoss = 0
            for i in range(0, 3):
                healthLoss = healthLoss + damageDone[i]
            healthC1 = healthC1 - healthLoss
            
            #lifesteal
            if c2AttackArray[index2][3] == 0:
                healthC2 = healthC2 + c2Stats[7] * damageDone[0]
            
            #healthRegen - future check if grievious wounds
            healthC1 = healthC1 + (c1Stats[1] / 5) * (nextMove1 - timeAt)
            healthC2 = healthC2 + (c2Stats[1] / 5) * (nextMove1 - timeAt)
            
            index1 = index1 + 1
            index2 = index2 + 1
            timeAt = nextMove1
        
        if healthC1 < 0:
            print("Champion 1 is dead.")
            print("Champion 2 had " + str(healthC2) + " health remaining.")
            print("The battle took " + str(timeAt) + " seconds to complete.")
            break;
        
        if healthC2 < 0:
            print("Champion 2 is dead.")
            print("Champion 1 had " + str(healthC1) + " health remaining.")            
            print("The battle took " + str(timeAt) + " seconds to complete.")
            break;
    
    healthMetric = healthC1 / c1Stats[0]
    
    return healthMetric
        
