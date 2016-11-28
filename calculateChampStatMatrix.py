# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:22:10 2016

@author: Max
"""
#given an item id return the item matrix
#1029

def id2StatMatrix(id):
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['stats'];

"""  MAY be neccesary for ultimate integration
champStatMatrix=[0,0,0,0,0,0,0,0,0];
# CHAMP STAT Matrix - Health, ARmor, Magic Resist, Attack Damadge, Attack Speed, Range
def genChampionStatMatrix(build, baseStat):
    global champStatMatrix;
    numOfItems = build.getOpenSlots();
    for itemIndex in range(0,numOfItems):
        champStatMatrix = champStatMatrix + id2StatMatrix(build.getSlot(itemIndex)[0]);
"""     
        
#Example
itemA =[3085,"armor",300];
xy = possibleBuild(itemA,0,0,0,0,0,100);

print(xy.getSlot(0)[0]);
print(id2StatMatrix(xy.getSlot(0)[0]));

    