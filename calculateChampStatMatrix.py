# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:22:10 2016

@author: Max
"""
from copy import copy, deepcopy;
##INDEXING FOR STAT ARRAYS
HEALTH = 0;
HEALTH_REGEN=1;
ARMOR  = 2;
MAGIC_RESIST=3;
ATTACK_DAMADGE=4;
ATTACK_SPEED=5;
CRIT_STRIKE=6;
LIFE_STEAL=7;
ATTACK_SPEED_OFFSET=8;
LEVEL=8;

#given an item id return the item matrix
#1029
def id2StatMatrix(id):
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['stats'];

#takes an item stat matrix, parses the different attributes and applies them
#to the champ StatMatrix
#newChampStat =0;
def itemAndChamp2StatMatrix(champStatMatrix, itemStats):
        global newChampStat;
        newChampStat = deepcopy(champStatMatrix);
       # newChampStat[ATTACK_SPEED]=newChampStat[ATTACK_SPEED_OFFSET]+newChampStat[ATTACK_SPEED]*newChampStat[ATTACK_SPEED_OFFSET];
        #print("new as", newChampStat[ATTACK_SPEED]);        
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
        return newChampStat;
        

cStatMatrix=[0,0,0,0,0,0,0,0,0];
# CHAMP STAT Matrix - Health, HealthRegen, Armor, Magic Resist, Attack Damadge, 
#Attack Speed, Crit strike, Life Steal, AttackSpeed Offset, level
def genChampionStatMatrix(baseStat, build):
    global cStatMatrix;
   # cStatMatrix = deepcopy(baseStat);
    cStatMatrix=[baseStat[0],baseStat[1],baseStat[2],baseStat[3],
                 baseStat[4],baseStat[5],baseStat[6],baseStat[7],baseStat[9]];
    numOfItems = 6- build.getOpenSlots();
    for itemIndex in range(0,numOfItems):
        cStatMatrix = itemAndChamp2StatMatrix(cStatMatrix, id2StatMatrix(build.getSlot(itemIndex)[0]));
    return cStatMatrix;
     
        
#Example
        #Ruined King
#itemA =[3153,"runied king", --99];   #id only accurate on these entries



"""
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
    id == 3031 or #infinty edge                         todo  250% crit
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
    id == 3508):#ess reav 
"""


itemA=[3508, "cloth armor", -99];
# Infinity edge
itemB=[3086, "infinity Edge", -99]
xy = possibleBuild(itemA,itemB,0,0,0,0,100);
BaseCharacterStats = [500,5.67,22.9,30,60,.568,0,0,.568,3];

#print(xy.getSlot(0)[0]);
#print(id2StatMatrix(xy.getSlot(0)[0]));
#print(id2StatMatrix(xy.getSlot(1)[0]));
#print(BaseCharacterStats);
#print(genChampionStatMatrix(BaseCharacterStats,xy));

'''
print(xy.getSlot(1)[0]);
print((id2StatMatrix(xy.getSlot(1)[0])).keys());
print(BaseCharacterStats);
print("ok");
print(itemAndChamp2StatMatrix(BaseCharacterStats, id2StatMatrix(xy.getSlot(0)[0])));
print(BaseCharacterStats);
print(genChampionStatMatrix(BaseCharacterStats,xy));
'''

    