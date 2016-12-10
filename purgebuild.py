# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 07:47:36 2016

@author: JK Rutter
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
noDuplicates = [
2015, 3031, 3034, 3036, 3035, 3044, 3046, 3057, 3072, 3078, 3085, 3094, 3087, 3508
]

mutuallyExclusive = [
[2015, 3094],
[2015, 3087],
[3094, 3087],
[3101, 3078],
[3044, 3078],
[3057, 3078],
[3034, 3036]
]

def purgeBuild(itemArray):
    readytogo = True
    
    for i in range(0, len(noDuplicates)):
        counter = 0
        for j in range(0, len(itemArray)):
            if itemArray[j] == noDuplicates[i]:
                counter = counter + 1
        if counter > 1:
            readytogo = False
            break
    
    if readytogo:
        for i in range(0, len(mutuallyExclusive)):
            firstItem = False
            secondItem = False
            for j in range(0, len(ItemArray)):
                if itemArray[j] == mutuallyExclusive[i][0]:
                    firstItem = True
                if itemArray[j] == mutuallyExclusive[i][1]:
                    secondItem = True
            if firstItem and secondItem:
                readytogo = False
                break
            
    return readytogo