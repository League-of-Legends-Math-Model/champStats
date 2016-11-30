# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:52:34 2016

@author: JK Rutter
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

def caitAttackArray(statMatr):
    sequence = np.zeros(shape=(2, 15))

    # if infinity edge, critDamage = 2.5    
    critDamage = 2    
        
    oneShotEnhance = 0
    regOnHit = 0
    
    abilityPoints = [0, 0, 0, 0]
    
    for i in range(0, statMatr[8]):
        abilityPoints[caitAbSequence[i]-1] = abilityPoints[caitAbSequence[i]-1] + 1
    headshot = statMatr[4] + (.5 + .5 * critDamage * statMatr[6])*statMatr[4]
    critHeadshot = headshot + statMatr[4] * (critDamage - 1)
    trapHeadshot = headshot + 30 + (abilityPoints[1] - 1) * 40 + .7 * statMatr[4]    
    trapCritHS = trapHeadshot + statMatr[4] * (critDamage - 1)
    caliberNet = 70 + (abilityPoints[2] - 1) * 40
    peacemaker = 30 + (abilityPoints[0] - 1) * 40 + (1.3 + .1 * (abilityPoints[0] - 1)) * statMatr[4]
    
    for i in range(0, 15):
        sequence[0][i] = 1 / statMatr[5]
    
    critted = rng.random()
    
    sequence[1][0] = trapHeadshot + oneShotEnhance + regOnHit
    
    if critted <= statMatr[6]:
        sequence[1][0] = trapCritHS + oneShotEnhance + regOnHit
    
    sequence[0][1] = 0.25
    sequence[1][1] = caliberNet
    
    sequence[1][2] = headshot + regOnHit
    
    critted = rng.random()
    
    if critted <= statMatr[6]:
        sequence[1][2] = critHeadshot + regOnHit
    
    critted = rng.random()
    sequence[1][3] = headshot + regOnHit
    if critted <= statMatr[6]:
        sequence[1][3] = critHeadshot + regOnHit
    
    for i in range(4, 15):
        critted = rng.random()
        sequence[1][i] = statMatr[4] + regOnHit
        if critted <= statMatr[6]:
            sequence[1][i] = statMatr[4] * 2.5 + regOnHit
    
    critted = rng.random()
    sequence[1][10] = headshot + regOnHit
    if critted <= statMatr[6]:
        sequence[1][10] = critHeadshot + regOnHit
        
    # other item changes
    
    return sequence

def calcDPS(caitSeq):
    time = 0
    damage = 0    
    for i in range(0, 15):
        time = time + caitSeq[0][i]
        damage = damage + caitSeq[1][i]
    return damage / time