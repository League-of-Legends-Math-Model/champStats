# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:36:45 2016

@author: JK Rutter
"""
import math
import numpy as np
"""
Character Array : [Health, Health Regen, Mana, Mana Regen, Attack Damage, Attack Speed, Armor, Magic Resist, Range, Movement Speed]
"""


def Sivir():
    return np.array([515.76, 5.17, 284, 8.01, 57.46, 0.625, 22.21, 30, 500, 335])

def SivirGrowth():
    return np.array([82, 0.55, 50, 0.9, 2.41, .016, 3.25, 0, 0, 0])

def Kindred():
    return np.array([540, 7, 300, 6.95, 54.42, 0.625, 20, 30, 500, 325])

def KindredGrowth():
    return np.array([85, 0.55, 35, 0.4, 1.61, 0.025, 3.5, 0, 0, 0])

def growth(charBase, charGrowth, level):
    return charBase + charGrowth * (level - 1) * (0.685 + 0.0175 * level)

lifestealB = 0
lifestealA = 0

"""
Item Array : [Health, Health Regen, Mana, Mana Regen, Attack Damage, Attack Speed, Armor, Magic Resist, Movement Speed, Life Steal, Spell Vamp, others?]
"""

def modelAitems():
    return np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def LongSword(itemarray):
    itemarray[4] += 15
    return itemarray

def Pickaxe(itemarray):
    itemarray[4] += 25
    return itemarray
    
def RubyCrystal(itemarray):
    itemarray[0] += 150
    return itemarray
    
def modelBitems():
    return np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

setupA = modelAitems()
setupA = LongSword(setupA)
setupA = LongSword(setupA)
setupB = modelBitems()
setupB = Pickaxe(setupB)

for i in range(1, 19):
    modelA = growth(Sivir(), SivirGrowth(), i)
    modelB = growth(Kindred(), KindredGrowth(), i)
    modelArawAD = round(modelA.item(4) + setupA.item(4)) * (modelA.item(5) + setupA.item(5))
    modelBrawAD = round(modelB.item(4) + setupB.item(4)) * (modelB.item(5) + setupB.item(5))
    modelBHP = round(modelB.item(0)+setupB.item(0))
    modelAHP = round(modelA.item(0)+setupA.item(0))
    modelAArmor = 100 / (100 + modelA.item(6) + setupA.item(6))
    modelBArmor = 100 / (100 + modelB.item(6) + setupB.item(6))
    modelAHPRegen = modelA.item(1) + setupA.item(1)
    modelBHPRegen = modelB.item(1) + setupB.item(1)
    cKillf = modelBHP / ((modelArawAD) * modelBArmor - lifestealB - modelBHPRegen / 5)
    fKillc = modelAHP / ((modelBrawAD) * modelAArmor - lifestealA - modelAHPRegen / 5)
    print("At Level: " + str(i))
    print("Time for Sivir to kill Kindred: " + str(cKillf))
    print("Time for Kindred to kill Sivir: " + str(fKillc))
    print("Sivir Instantaneous DPS: " + str(modelArawAD))
    print("Kindred Instantaneous DPS: " + str(modelBrawAD))
    print("")
