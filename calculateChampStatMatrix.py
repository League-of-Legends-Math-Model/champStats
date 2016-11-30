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
                print(-99);  #ToDO 
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
                print(-99);  #ToDO 
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
    cStatMatrix = deepcopy(baseStat);
    numOfItems = 6- build.getOpenSlots();
    for itemIndex in range(0,numOfItems):
        cStatMatrix = itemAndChamp2StatMatrix(cStatMatrix, id2StatMatrix(build.getSlot(itemIndex)[0]));
    return cStatMatrix;
     
        
#Example
        #Ruined King
#itemA =[3153,"runied king", --99];   #id only accurate on these entries

itemA=[1029, "cloth armor", -99];
# Infinity edge
itemB=[3031, "infinity Edge", -99]
xy = possibleBuild(itemA,itemB,0,0,0,0,100);
BaseCharacterStats = [500,5.67,22.9,30,60,.568,0,0,.568,3];

print(xy.getSlot(0)[0]);
print(id2StatMatrix(xy.getSlot(0)[0]));
print(xy.getSlot(1)[0]);
print((id2StatMatrix(xy.getSlot(1)[0])).keys());
print(BaseCharacterStats);
print("ok");
print(itemAndChamp2StatMatrix(BaseCharacterStats, id2StatMatrix(xy.getSlot(0)[0])));
print(BaseCharacterStats);
print(genChampionStatMatrix(BaseCharacterStats,xy));


    