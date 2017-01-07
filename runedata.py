# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:19:07 2017

@author: Jon-Michael

partype will tell you what their secondary bar is.
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
    32 - BASE PERCENT MITIGATION
    33 - BASE PERCENT ABILITY INCREASE
    34 - BASE PERCENT ALL DAMAGE INCREASE
    35 - CRIT DAMAGE (base 200%)
    36 - BONUS ATTACK SPEED
"""

"""
RUNE STATS THAT APPEAR:  (A 0: in front means there are no corresponding runes)
FlatArmorMod	double	
0:FlatAttackSpeedMod	double	
0:FlatBlockMod	double	
FlatCritChanceMod	double	
FlatCritDamageMod	double	
0:FlatEXPBonus	double	
FlatEnergyPoolMod	double	
FlatEnergyRegenMod	double	
FlatHPPoolMod	double	
FlatHPRegenMod	double	
FlatMPPoolMod	double	
FlatMPRegenMod	double	
FlatMagicDamageMod	double	
0:FlatMovementSpeedMod	double	
FlatPhysicalDamageMod	double	
FlatSpellBlockMod	double	
0:PercentArmorMod	double	
PercentAttackSpeedMod	double	
0:PercentBlockMod	double	
0:PercentCritChanceMod	double	
0:PercentCritDamageMod	double	
0:PercentDodgeMod	double	
PercentEXPBonus	double         NOT CURRENTLY IMPLEMENTED - warning?	
PercentHPPoolMod	double	
0:PercentHPRegenMod	double	
PercentLifeStealMod	double	
0:PercentMPPoolMod	double	
0:PercentMPRegenMod	double	
0:PercentMagicDamageMod	double	
PercentMovementSpeedMod	double	
0:PercentPhysicalDamageMod	double	
0:PercentSpellBlockMod	double	
PercentSpellVampMod	double	
rFlatArmorModPerLevel	double	
0:rFlatArmorPenetrationMod	double	
0:rFlatArmorPenetrationModPerLevel	double	
0:rFlatCritChanceModPerLevel	double	
0:rFlatCritDamageModPerLevel	double	
0:rFlatDodgeMod	double	
0:rFlatDodgeModPerLevel	double	
rFlatEnergyModPerLevel	double	
rFlatEnergyRegenModPerLevel	double	
rFlatGoldPer10Mod	double	        NOT CURRENTLY IMPLEMENTED
rFlatHPModPerLevel	double	
rFlatHPRegenModPerLevel	double	
rFlatMPModPerLevel	double	
rFlatMPRegenModPerLevel	double	
rFlatMagicDamageModPerLevel	double	
rFlatMagicPenetrationMod	double	
0:rFlatMagicPenetrationModPerLevel	double	
0:rFlatMovementSpeedModPerLevel	double	
rFlatPhysicalDamageModPerLevel	double	
rFlatSpellBlockModPerLevel	double	
0:rFlatTimeDeadMod	double	
0:rFlatTimeDeadModPerLevel	double	
0:rPercentArmorPenetrationMod	double	
0:rPercentArmorPenetrationModPerLevel	double	
0:rPercentAttackSpeedModPerLevel	double	
rPercentCooldownMod	double	
rPercentCooldownModPerLevel	double	
0:rPercentMagicPenetrationMod	double	
0:rPercentMagicPenetrationModPerLevel	double	
0:rPercentMovementSpeedModPerLevel	double	
rPercentTimeDeadMod	double	        NOT CURRENTLY IMPLEMENTED
0:rPercentTimeDeadModPerLevel	double
"""
def runeStats(runeArray, baseStatArray, level, partype, percents):
    for i in range(0, len(runeArray)):
        rStat = runeArray[i]
        number = rStat['count']
        runeID = rStat['runeId']
        runeUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/rune/"+str(runeID)+"?runeData=stats&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
        response = requests.get(runeUrl)
        allRune = response.json()
        stats = allRune['stats']
        """
            LETHALITY CALCULATION
            8013 - 2.96 LETHALITY
            5221 - 2.49 LETHALITY
            8020 - 3.20 LETHALITY
            5253 - 1.60 LETHALITY
            5343 - 3.20 LETHALITY
            5131 - 1.25 LETHALITY
            5009 - .9 LETHALITY
            5099 - 1.78 LETHALITY
        """
        #flats
        if percents == False:
            if runeID == 8013:
                baseStatArray[22] = baseStatArray[22] + 2.96 * number
            if runeID == 5221:
                baseStatArray[22] = baseStatArray[22] + 2.49 * number
            if runeID == 8020:
                baseStatArray[22] = baseStatArray[22] + 3.20 * number
            if runeID == 5253:
                baseStatArray[22] = baseStatArray[22] + 1.60 * number
            if runeID == 5343:
                baseStatArray[22] = baseStatArray[22] + 3.20 * number
            if runeID == 5131:
                baseStatArray[22] = baseStatArray[22] + 1.25 * number
            if runeID == 5009:
                baseStatArray[22] = baseStatArray[22] + .9 * number
            if runeID == 5099:
                baseStatArray[22] = baseStatArray[22] + 1.78 * number
            baseStatArray[15] = baseStatArray[15] + stats['FlatArmorMod'] * number
            baseStatArray[11] = baseStatArray[11] + stats['FlatCritChanceMod'] * number
            baseStatArray[35] = baseStatArray[35] + stats['FlatCritDamageMod'] * number
            baseStatArray[0] = baseStatArray[0] + stats['FlatHPPoolMod'] * number 
            baseStatArray[2] = baseStatArray[2] + stats['FlatHPRegenMod'] * number
            baseStatArray[20] = baseStatArray[20] + stats['FlatMagicDamageMod'] * number
            baseStatArray[8] = baseStatArray[8] + stats['FlatPhysicalDamageMod'] * number
            baseStatArray[17] = baseStatArray[17] + stats['FlatSpellBlockMod'] * number
            baseStatArray[36] = baseStatArray[36] + stats['PercentAttackSpeedMod'] * number    
            baseStatArray[30] = baseStatArray[30] + stats['PercentLifeStealMod'] * number
            baseStatArray[31] = baseStatArray[31] + stats['PercentSpellVampMod'] * number
            baseStatArray[0] = baseStatArray[0] + stats['rFlatHPModPerLevel'] * number * level
            baseStatArray[2] = baseStatArray[2] + stats['rFlatHPRegenModPerLevel'] * number * level
            baseStatArray[20] = baseStatArray[20] + stats['rFlatMagicDamageModPerLevel'] * number * level
            baseStatArray[25] = baseStatArray[25] + stats['rFlatMagicPenetrationMod'] * number
            baseStatArray[8] = baseStatArray[8] + stats['rFlatPhysicalDamageModPerLevel'] * number * level
            baseStatArray[17] = baseStatArray[17] + stats['rFlatSpellBlockModPerLevel'] * number * level
            baseStatArray[29] = baseStatArray[29] + stats['rPercentCooldownMod'] * number
            baseStatArray[29] = baseStatArray[29] + stats['rPercentCooldownModPerLevel'] * number * level

            if partype == "Energy":
                baseStatArray[4] = baseStatArray[4] + stats['FlatEnergyPoolMod'] * number
                baseStatArray[6] = baseStatArray[6] + stats['FlatEnergyRegenMod'] * number
                baseStatArray[4] = baseStatArray[4] + stats['rFlatEnergyModPerLevel'] * number * level
                baseStatArray[6] = baseStatArray[6] + stats['rFlatEnergyRegenModPerLevel'] * number * level
            if partype == "MP":
                baseStatArray[4] = baseStatArray[4] + stats['FlatMPPoolMod'] * number
                baseStatArray[6] = baseStatArray[6] + stats['FlatMPRegenMod'] * number
                baseStatArray[4] = baseStatArray[4] + stats['rFlatMPModPerLevel'] * number * level
                baseStatArray[6] = baseStatArray[6] + stats['rFlatMPRegenModPerLevel'] * number * level



            #perlevels
            baseStatArray[15] = baseStatArray[15] + stats['rFlatArmorModPerLevel'] * number * level


        #percentages
        if percents == True:
            baseStatArray[0] = baseStatArray[0] * (1 + stats['PercentHPPoolMod'] * number)
            baseStatArray[19] = baseStatArray[19] * (1 + stats['PercentMovementSpeedMod'] * number)
        
    return baseStatArray




