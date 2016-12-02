# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:09:50 2016

@author: JK Rutter
"""

# itempull

dpsArray = [[[0, 0, 0, 0, 0, 0], 0]]
level = 3
gold = 1000

detBuilds = determinePossibleBuilds(gold)

cStats = caitStats(level)

for i in range(0, len(detBuilds)):
    stats = genChampionStatMatrix(cStats, detBuilds[i])
    items = detBuilds[i].getItems()
    print("st",stats);
    print("it",items);
    seq = caitAttackArray(stats, items)
    
    dps = calcDPS(seq)
    
    temp = [detBuilds[i].getItems(), dps]
    
    dpsArray.append([temp])

