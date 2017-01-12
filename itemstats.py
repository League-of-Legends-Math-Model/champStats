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

#onHitItems = [0item ID, 1name, 2damage type, 3base, 4base AD,
#5bonus AD, 6total AD, 7AP, 8max health, 9enemy max health, 
#10level bonus, CD, lethality, mana]
onHitItems = [
[1410, "Runic Echoes", 1, 60, 0, 0, 0, .1, 0, 0, 0, 0, 0, 0],
[1414, "Runic Echoes", 1, 60, 0, 0, 0, .1, 0, 0, 0, 0, 0, 0],
[1402, "Runic Echoes", 1, 60, 0, 0, 0, .1, 0, 0, 0, 0, 0, 0],
[3673, "Runic Echoes", 1, 60, 0, 0, 0, .1, 0, 0, 0, 0, 0, 0],
[3087, "Statikk Shiv", 1, 45.89, 0, 0, 0, 0, 0, 0, 4.11, 0, 0, 0],
[3085, "Runaan's Hurricane", 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1419, "Bloodrazor", 0, 0, 0, 0, 0, 0, 0, .04, 0, 0, 0, 0],
[1418, "Bloodrazor", 0, 0, 0, 0, 0, 0, 0, .04, 0, 0, 0, 0],
[1416, "Bloodrazor", 0, 0, 0, 0, 0, 0, 0, .04, 0, 0, 0, 0],
[3675, "Bloodrazor", 0, 0, 0, 0, 0, 0, 0, .04, 0, 0, 0, 0],
[3285, "Luden's Echo", 1, 100, 0, 0, 0, .1, 0, 0, 0, 0, 0, 0],
[3094, "Rapid Firecannon", 1, 43.53, 0, 0, 0, 0, 0, 0, 6.47, 0, 0, 0],
[2015, "Kircheis Shard", 1, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[3091, "Wit's End", 1, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[3092, "Frost Queen's Claim", 1, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[3742, "Dead Man's Plate", 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[3748, "Titanic Hydra", 0, 5, 0, 0, 0, 0, .01, 0, 0, 0, 0, 0],
[3100, "Lich Bane", 1, 0, 0, 0, -.25, .5, 0, 0, 0, 1.5, 0, 0],
[3147, "Duskblade of Draktharr", 2, 50, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0],
[3042, "Muramana", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .06],
[3043, "Muramana", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .06],
[3151, "Liandry's Torment", 1, 0, 0, 0, 0, 0, 0, .06, 0, 0, 0, 0],
[3145, "Hextech Revolver", 1, 45.59, 0, 0, 0, 0, 0, 0, 4.41, 40, 0, 0],
[3025, "Iceborn Gauntlet", 0, 0, 0, 0, 1, 0, 0, 0, 0, 1.5, 0, 0],
[3115, "Nashor's Tooth", 1, 15, 0, 0, 0, .15, 0, 0, 0, 0, 0, 0],
[3122, "Wicked Hatchet", 1, 0, 0, .6, 0, 0, 0, 0, 0, 0, 0, 0],
[3057, "Sheen", 0, 0, 1, 0, 0, 0, 0, 0, 0, 1.5, 0, 0],
[1043, "Recurve Bow", 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[3122, "Lightbringer", 1, 0, 0, .9, 0, 0, 0, 0, 0, 0, 0, 0],
[3078, "Trinity Force", 0, 0, 2, 0, 0, 0, 0, 0, 0, 1.5, 0, 0]
]

#cdrRegenItems = [item ID, hp regen, mp regen, cdr, gain HP regen = mp regen(1 = yes, 0 = no)]
#check to see if CDR is already .05; calc bonus MP regen after the loop

cdrRegenItems = [
[3084, 1, 0, 0, 0],
[1412, 0, 0, .1, 0],
[1408, 0, 0, .1, 0],
[1400, 0, 0, .1, 0],
[3671, 0, 0, .1, 0],
[3083, 2, 0, .1, 0],
[3098, 0, .75, 0, 0],
[3097, .5, 0, 0, 0],
[3096, .25, .75, 0, 0],
[3092, 0, .75, .1, 0],
[3748, 1, 0, 0, 0],
[2303, 2, 0, 0, 0],
[2301, 0, 1, .1, 0],
[2302, 1, 1, .1, 0],
[1056, 0, .5, 0, 0],
[3110, 0, 0, .2, 0],
[3107, .75, .75, .1, 0],
[3109, 1, 0, 0, 0],
[3108, 0, 0, .1, 0],
[3102, 1, 0, 0, 0],
[3104, 0, 0, .1, 0],
[3100, 0, 0, .1, 0],
[3101, 0, 0, .1, 0],
[3812, 0, 0, .1, 0],
[3801, .5, 0, 0, 0],
[3800, 1, 0, 0, 0],
[3504, 0, .5, .1, 0],
[3508, 0, 0, .1, 0],
[1004, 0, .25, 0, 0],
[1006, .5, 0, 0, 0],
[3156, 0, 0, .1, 0],
[3152, 0, 0, .1, 0],
[3137, 0, 0, .1, 0],
[3001, 0, 0, .1, 0],
[3142, 0, 0, .1, 0],
[3028, 0, .5, 0, 1],
[3222, 0, 1, .1, 1],
[3133, 0, 0, .1, 0],
[3114, 0, .5, .1, 0],
[3115, 0, 0, .2, 0],
[3024, 0, 0, .1, 0],
[2053, 1.25, 0, 0, 0],
[3050, 0, 0, .1, 0],
[3056, 1.5, 0, .1, 0],
[3301, 0, .25, .1, 0],
[3303, 0, .25, 0, 0],
[3187, 0, 0, .2, 0],
[3069, 1.5, 0, 0, 0],
[3071, 0, 0, .2, 0],
[3174, 0, .75, 0, 1],
[3078, 0, 0, .2, 0],
[3158, 0, 0, .1, 0],
[3157, 0, 0, .1, 0],
[3060, 0, 0, .1, 0],
[3165, 0, 0, .2, 0],
[3065, 2, 0, .1, 0],
[3067, 0, 0, .1, 0]
]

#lethalMoveItems = [item ID, name, lethality, %movement speed increase,
#sit. flat, sit. %, stolen movement, slow resist, tenacity]
lethalMoveItems = [
[3086, "Zeal", 0, .05, 0, 0, 0, 0, 0],
[3742, "Dead Man's Plate", 0, 0, 60, 0, 0, 0, 0],
[3109, "Knight's Vow", 0, 0, 0, .15, 0, 0, 0],
[3252, "Poacher's Dirk", 0, 0, 20, 0, 0, 0, 0],
[3814, "Edge of Night", 15, 0, 20, 0, 0, 0, 0],
[3706, "Stalker's Blade", 0, 0, 0, 0, .2, 0, 0],
[3800, "Righteous Glory", 0, 0, 0, .75, 0, 0, 0],
[3147, "Duskblade of Draktharr", 15, 0, 20, 0, 0, 0, 0],
[3009, "Boots of Swiftness", 0, 0, 0, 0, 0, .25, 0],
[3153, "Blade of the Ruined King", 0, 0, 0, 0, .25, 0, 0],
[3139, "Mercurial Scimitar", 0, 0, 0, .5, 0, 0, 0],
[3137, "Dervish Blade", 0, 0, 0, .5, 0, 0, 0],
[3142, "Youmuu's Ghostblade", 20, 0, 0, .2, 0, 0, 0],
[3512, "Zz'rot Portal", 0, 0, 0, .2, 0, 0, 0],
[3222, "Mikael's Crucible", 0, 0, 0, .4, 0, 0, 0],
[3134, "Serrated Dirk", 10, 0, 20, 0, 0, 0, 0],
[3113, "Aether Wisp", 0, .5, 0, 0, 0, 0, 0],
[3117, "Boots of Mobility", 0, 0, 90, 0, 0, 0, 0],
[2053, "Raptor Cloak", 0, 0, 0, .2, 0, 0, 0],
[3056, "Ohmwrecker", 0, 0, 0, .2, 0, 0, 0],
[3044, "Phage", 0, 0, 60, 0, 0, 0, 0],
[3046, "Phantom Dancer", 0, .07, 0, 0, 0, 0, 0],
[3071, "Black Cleaver", 0, 0, 60, 0, 0, 0, 0],
[3078, "Trinity Force", 0, 0, 60, 0, 0, 0, 0],
[3170, "Moonflair Spellblade", 0, 0, 0, 0, 0, 0, .35],
[3111, "Mercury's Treads", 0, 0, 0, 0, 0, 0, .3],
[3504, "Ardent Censer", 0, .08, 0, 0, 0, 0, 0]


]