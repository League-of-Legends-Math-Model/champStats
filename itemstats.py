# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 08:25:54 2017

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
Item Stats that appear: (A 0: in front means there are no corresponding items)
FlatArmorMod	double	
0:FlatAttackSpeedMod	double	
0:FlatBlockMod	double	
FlatCritChanceMod	double	
0:FlatCritDamageMod	double	
0:FlatEXPBonus	double	
0:FlatEnergyPoolMod	double	
0:FlatEnergyRegenMod	double	
FlatHPPoolMod	double	
FlatHPRegenMod	double	
FlatMPPoolMod	double	
FlatMPRegenMod	double	
FlatMagicDamageMod	double	
FlatMovementSpeedMod	double	
FlatPhysicalDamageMod	double	
FlatSpellBlockMod	double	
0:PercentArmorMod	double	
PercentAttackSpeedMod	double	
0:PercentBlockMod	double	
0:PercentCritChanceMod	double	
0:PercentCritDamageMod	double	
0:PercentDodgeMod	double	
0:PercentEXPBonus	double	
0:PercentHPPoolMod	double	
0:PercentHPRegenMod	double	
PercentLifeStealMod	double	
0:PercentMPPoolMod	double	
0:PercentMPRegenMod	double	
0:PercentMagicDamageMod	double	
PercentMovementSpeedMod	double	
0:PercentPhysicalDamageMod	double	
0:PercentSpellBlockMod	double	
0:PercentSpellVampMod	double	
0:rFlatArmorModPerLevel	double	
0:rFlatArmorPenetrationMod	double	
0:rFlatArmorPenetrationModPerLevel	double	
0:rFlatCritChanceModPerLevel	double	
0:rFlatCritDamageModPerLevel	double	
0:rFlatDodgeMod	double	
0:rFlatDodgeModPerLevel	double	
0:rFlatEnergyModPerLevel	double	
0:rFlatEnergyRegenModPerLevel	double	
0:rFlatGoldPer10Mod	double	
0:rFlatHPModPerLevel	double	
0:rFlatHPRegenModPerLevel	double	
0:rFlatMPModPerLevel	double	
0:rFlatMPRegenModPerLevel	double	
0:rFlatMagicDamageModPerLevel	double	
0:rFlatMagicPenetrationMod	double	
0:rFlatMagicPenetrationModPerLevel	double	
0:rFlatMovementSpeedModPerLevel	double	
0:rFlatPhysicalDamageModPerLevel	double	
0:rFlatSpellBlockModPerLevel	double	
0:rFlatTimeDeadMod	double	
0:rFlatTimeDeadModPerLevel	double	
0:rPercentArmorPenetrationMod	double	
0:rPercentArmorPenetrationModPerLevel	double	
0:rPercentAttackSpeedModPerLevel	double	
0:rPercentCooldownMod	double	
0:rPercentCooldownModPerLevel	double	
0:rPercentMagicPenetrationMod	double	
0:rPercentMagicPenetrationModPerLevel	double	
0:rPercentMovementSpeedModPerLevel	double	
0:rPercentTimeDeadMod	double	
0:rPercentTimeDeadModPerLevel	double
"""

def itemStats(itemArray, baseStatArray, partype, percents):
    
    for i in range(0, len(itemArray)):
        if percents:
            itemID = itemArray[i]
            itemUrl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(itemID)+"?itemData=stats&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
            response = requests.get(itemUrl)
            itemData = response.json()
            itemstat = itemData['stats']
            baseStatArray[15] = baseStatArray[15] + itemstat['FlatArmorMod']
            baseStatArray[11] = baseStatArray[11] + itemstat['FlatCritChanceMod']
            baseStatArray[0] = baseStatArray[0] + itemstat['FlatHPPoolMod']
            baseStatArray[2] = baseStatArray[2] + itemstat['FlatHPRegenMod']
            baseStatArray[20] = baseStatArray[20] + itemstat['FlatMagicDamageMod']
            baseStatArray[19] = baseStatArray[19] + itemstat['FlatMovementSpeedMod']
            baseStatArray[8] = baseStatArray[8] + itemstat['FlatPhysicalDamageMod']
            baseStatArray[17] = baseStatArray[17] + itemstat['FlatSpellBlockMod']
            baseStatArray[36] = baseStatArray[36] + itemstat['PercentAttackSpeedMod']
            baseStatArray[30] = baseStatArray[30] + itemstat['PercentLifeStealMod']
            if partype == "MP":
                baseStatArray[4] = baseStatArray[4] + itemstat['FlatMPPoolMod']
                baseStatArray[6] = baseStatArray[6] + itemstat['FlatMPRegenMod']
        else:
            baseStatArray[19] = baseStatArray[19] * (1 + itemstat['PercentMovementSpeedMod'])

    return baseStatArray

"""
UNACCOUNTED FOR ITEM EFFECTS, STATS, ETC.
+ - Calculate
- - Warning
On Hits (EVERY HIT / TRIGGERED ON HIT)+

EVERY HIT+
Muramana
Recurve Bow


TRIGGERED ON HIT+
Sheen
Trinity Force


Activatables (damage)+

Activatables (shield)+

Activatables (movement speed)-

Activatables (slow)-

HP/MP Regen, Base AD+

lethality+

Percentage based (rabadons, cinderhulk, essence reaver)+

Cooldown Reduction (max 45% with masteries; 40% from items)+

Movement Speed+

Reductions (attack speed, crit damage)-

AOE (immolate, gauntlet, redemption)+

auras-

tenacity/slow resist+

viktor's hex core+

debuff remover (quicksilver)-

stacking abilities (guinsoo's, sanguine, roa)+ (full stacks)

minion enhance (zzrot, banner of command)-

grievous wounds (morello, mortal reminder)-

dash (hextech)-

bleed (wicked hatchet)+

enemy hp (lord d regards, etc.)+

link items (zeke's, knight's vow)-

reduction (phantom dancer)+

shield/heal (unholy, censer)+

aoe attacks (ravenous, runaan's)-

thornmail-

statis-

item active cdr (ruby sightstone)+
"""

#warningItems = [item ID, cd (if applicable), warning]
warningItems = [
[3085, 0, "This unit shoots at 3 units at a time."],
[3083, 8, "This unit regenerates 15% of max health every 5 seconds."],
[]
]