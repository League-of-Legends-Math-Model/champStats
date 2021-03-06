# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:09:50 2016

@author: JK Rutter
"""
import pickle;
import json
import requests
# itempull

dpsArray = []
level = 16
gold = 14000

fh = open('permFiles/buildPerm14000.txt', 'rb');
#fh = open('permFiles/perm1000.txt', 'rb');
up = pickle.Unpickler(fh);
detBuilds = up.load();


#detBuilds = determinePossibleBuilds(gold)
#ah = determinePossibleBuilds(400);
#print(ah[0].profile());
#print(detBuilds[0].profile());

cStats = caitStats(level)

#SIVIR GENERIC BUILD FOR TESTING
sStats = sivirStats(level)

#BUILDS
#sBuild = possibleBuild([3086,"recursive bow",-99], 0, 0, 0, 0, 0, 1000) #1000 Gold
#sBuild = possibleBuild([3086,"recursive bow",-99], [1042,"dagger",-99], [1051, "brawler's gloves", -99], 0, 0, 0, 2000) #2000 Gold
#sBuild = possibleBuild([3085, "runaan's hurricane", -99], [1036, "long sword",-99], 0, 0, 0, 0, 3000) #3000 Gold
sBuild = possibleBuild([3508, "essence reaver", -99], [3031, "infinity edge", -99], [3094, "rapid firecannon", -99], [3036, "lord dominik's regards", -99], [1038, "b.f. sword", -99], 0, 14000) #actually 13800 gold

sEnhancedStats = genChampionStatMatrix(sStats, sBuild)
sItems = sBuild.getItems()

sSeq = sivirAttackArray(sEnhancedStats, sItems)
#SIVIR GENERIC BUILD FOR TESTING

#QUINN GENERIC BUILD FOR TESTING
qStats = quinnStats(level)

#BUILDS
#qBuild = possibleBuild([1037, "pickaxe", -99], 0, 0, 0, 0, 0, 1000) #1000 Gold
#qBuild = possibleBuild([1037, "pickaxe", -99], [1018, "cloak of agility", -99], 0, 0, 0, 0, 2000) #2000 Gold
#qBuild = possibleBuild([1038, "b.f. sword", -99], [1037, "pickaxe", -99], [1018, "cloak of agility", -99], 0, 0, 0, 3000) #3000 Gold
qBuild = possibleBuild([3031, "infinity edge", -99], [3094, "rapid firecannon", -99], [3078, "trinity force", -99], [3072, "the bloodthirster", -99], [1042, "dagger", -99], 0, 14000) #actually 13933 gold
                        
qEnhancedStats = genChampionStatMatrix(qStats, qBuild)
qItems = qBuild.getItems()

qSeq = quinnAttackArray(qEnhancedStats, qItems)
#QUINN GENERIC BUILD FOR TESTING

finalMetric = []

for i in range(0, len(detBuilds)):    
    items = detBuilds[i].getItems()
    # filter out builds that can't work, which should save time on calculation
    purged = purgeBuild(items)
    if purged:    
        stats = genChampionStatMatrix(cStats, detBuilds[i])
        seq = caitAttackArray(stats, items)
    
        dps = calcDPS(seq, stats)

        sHealthMetric = battleDamage(seq, sSeq, stats, sEnhancedStats)
        qHealthMetric = battleDamage(seq, qSeq, stats, qEnhancedStats)
    
    #Quinn Health Metric
    
        temp = [detBuilds[i].getItems(), dps, sHealthMetric, qHealthMetric]
    
        dpsArray.append(temp)
    
totalDPS = 0

for i in range(0, len(dpsArray)):
    totalDPS = totalDPS + dpsArray[i][1]

averageDPS = totalDPS / len(dpsArray)

finalMetric = []

for i in range(0, len(dpsArray)):
    finalMetric.append([dpsArray[i][0], dpsArray[i][1], (dpsArray[i][1] - averageDPS)/averageDPS, dpsArray[i][2], dpsArray[i][3]])

#BEST DPS
organizeDPS = []

for i in range(0, len(finalMetric)):
    organizeDPS.append([finalMetric[i][1], i])

organizeDPS.sort(reverse=True)

print("Max DPS: " + str(organizeDPS[0][0]))

items = finalMetric[organizeDPS[0][1]][0]

for i in range(0, len(items)):
    name = "Empty"    
    if items[i] != 0:    
        itemurl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(int(items[i])) + "?itemData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
        response = requests.get(itemurl)
        buddy = response.json()
        name = buddy['name']
    print(name)

#BEST SIVIR SEQUENCE

organizeSivir = []

for i in range(0, len(finalMetric)):
    organizeSivir.append([finalMetric[i][3], i])

organizeSivir.sort(reverse=True)

print("Best Remaining Health vs. Sivir: " + str(organizeSivir[0][0]))

items = finalMetric[organizeSivir[0][1]][0]

for i in range(0, len(items)):
    name = "Empty"    
    if items[i] != 0:    
        itemurl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(int(items[i])) + "?itemData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
        response = requests.get(itemurl)
        buddy = response.json()
        name = buddy['name']
    print(name)

#BEST QUINN SEQUENCE

organizeQuinn = []
for i in range(0, len(finalMetric)):
    organizeQuinn.append([finalMetric[i][4], i])

organizeQuinn.sort(reverse=True)

print("Best Remaining Health vs. Quinn: " + str(organizeQuinn[0][0]))

items = finalMetric[organizeQuinn[0][1]][0]

for i in range(0, len(items)):
    name = "Empty"    
    if items[i] != 0:    
        itemurl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(int(items[i])) + "?itemData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
        response = requests.get(itemurl)
        buddy = response.json()
        name = buddy['name']
    print(name)

orgBestOverall = []

for i in range(0, len(finalMetric)):
    orgBestOverall.append([(finalMetric[i][2] + finalMetric[i][3] + finalMetric[i][4])/3, i])

orgBestOverall.sort(reverse=True)

print("Best Overall Metric: " + str(orgBestOverall[0][0]))

items = finalMetric[orgBestOverall[0][1]][0]

for i in range(0, len(items)):
    name = "Empty"    
    if items[i] != 0:    
        itemurl = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(int(items[i])) + "?itemData=all&api_key=836619ee-c877-45d9-b718-ab0eea4ed172"
        response = requests.get(itemurl)
        buddy = response.json()
        name = buddy['name']
    print(name)