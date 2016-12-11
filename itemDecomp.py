# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:41:19 2016

@author: Max
"""

from copy import copy, deepcopy;
import requests;
import pickle;
import json


#buildOrder =[];    
def determinePossibleBuildSequence(sobit,baseItems):
   # numberOfItemsInBank =3;
    global buildOrder;
    buildOrder =[];
    sizeOfBaseItemBank = sobit +1;
   # baseItemBank = [[0,0,0]];
    baseItemBank = baseItems;
    baseItemBank.extend([[0,0,0]]);
    i =0;
    while i < sizeOfBaseItemBank:
        print(i);
        j=i;
        while j < sizeOfBaseItemBank:
            if (j==i and j!=sizeOfBaseItemBank-1):
                j=j+baseItemBank[j][2];
                continue;
            k=j;
            while k < sizeOfBaseItemBank:
                if((k==j)and k!=sizeOfBaseItemBank-1):   #no duplicate!
                    k=k+baseItemBank[k][2];
                    continue;
                l=k;
                while l < sizeOfBaseItemBank:
                    if((l==k)and l!=sizeOfBaseItemBank-1):
                        l=l+baseItemBank[l][2];
                        continue;
                    m=l;
                    while m < sizeOfBaseItemBank:    
                        if((m==l)and m!=sizeOfBaseItemBank-1):
                            m=m+baseItemBank[m][2];
                            continue;    
                        buildOrder.append(possibleBuild(baseItemBank[i],
                                                       baseItemBank[j],
                                                       baseItemBank[k],
                                                       baseItemBank[l],
                                                       baseItemBank[m],0, 
(baseItemBank[i][1]+baseItemBank[j][1]+baseItemBank[k][1]+baseItemBank[l][1]+baseItemBank[m][1])));
                        m=m+1;
                    l=1+l;
                k=k+1;
            j=j+1;
        i=i+1;
    return buildOrder;
    
#takes in list of possible builds, sorts them into 
#[[1000],[2000],[3000],...[14000]]
#where [2000] contains a list of builds who cost x,  1000<x<2000 
def chunkByInterval(sequence):
    chunks=[[]for i in range(0,14)];
    for currentBuild in sequence:
        if(currentBuild.getGold()<1000):
            chunks[0].append(currentBuild);
            continue;
        if(currentBuild.getGold()<2000):
            chunks[1].append(currentBuild); 
            continue;
        if(currentBuild.getGold()<3000):
            chunks[2].append(currentBuild);
            continue;
        if(currentBuild.getGold()<4000):
            chunks[3].append(currentBuild);
            continue;
        if(currentBuild.getGold()<5000):
            chunks[4].append(currentBuild);
            continue;
        if(currentBuild.getGold()<6000):
            chunks[5].append(currentBuild);
            continue;
        if(currentBuild.getGold()<7000):
            chunks[6].append(currentBuild);
            continue;
        if(currentBuild.getGold()<8000):
            chunks[7].append(currentBuild);
            continue;
        if(currentBuild.getGold()<9000):
            chunks[8].append(currentBuild);
            continue;
        if(currentBuild.getGold()<10000):
            chunks[9].append(currentBuild); 
            continue;
        if(currentBuild.getGold()<11000):
            chunks[10].append(currentBuild);
            continue;
        if(currentBuild.getGold()<12000):
            chunks[11].append(currentBuild);
            continue;
        if(currentBuild.getGold()<13000):
            chunks[12].append(currentBuild);
            continue;
        if(currentBuild.getGold()<14000):
            chunks[13].append(currentBuild);
            continue;
    return chunks;


def buildChainCompatible(upper,lower):
    possibleComponents=decompBuild(upper);
    lowerComponents=lower.getItems();
    #print(lower.profile());
   # print("pos, low",possibleComponents, lowerComponents);
    for lowItem in lowerComponents:
        if(lowItem ==0):
            continue;
        found = False;
        for posItem in possibleComponents:
            if (str(lowItem) == str(posItem[0])):
                found = True;
        if(found != True):
            return False;
    return True;
    
#returns
def buildTrailerLink(build, chunks, goldStepLevel, chain):
    plausiblePrevSteps = [];
    startSegment = deepcopy(chain);
    if(goldStepLevel != 0): 
        for build in (chunks[goldStepLevel]):
            for prevStep in chunks[goldStepLevel-1]:
                if(buildChainCompatible(build,prevStep)):
                    #print("ss",startSegment);
                    newSegment = startSegment + [prevStep];
                    plausiblePrevSteps.append(newSegment);
                    #print("ns",newSegment);
    return plausiblePrevSteps;        

def buildTrailer(build, chunks, goldStepLevel):
    allChains = [[build]];
    levelChains =[];
    while goldStepLevel >0:
        print("gst:",goldStepLevel);
        levelChains =[];
        for currentChain in allChains:
            levelChains.append(buildTrailerLink(currentChain[0],
                             chunks,goldStepLevel,currentChain));
        goldStepLevel = goldStepLevel -1;
        allChains = levelChains;
        print("ac",allChains);
    return allChains;                         
            
#takes item id returns item name    
def id2Name(id):
    if(id == 0):
        id= 1052;  #FIX IN LONGTERM MODEL, THIS ACCOUNTS FOR 0 item
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['name'];
    
#take item id returns id's of all items it builds into immediately    
def id2Into(id):
    if(id == 0):
        id= 1052;  #FIX IN LONGTERM MODEL, THIS ACCOUNTS FOR 0 item
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['into'];

#takes item id and returns immediate predecessor items
def decompItem(id):
    if(id == 0):
        id= 1052;  #FIX IN LONGTERM MODEL, THIS ACCOUNTS FOR 0 item
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();
   # return list(currentItem.items())[0;
    #return currentItem['from'];
    for index in list(currentItem.items()):
        #return index[0];
        if(index[0] == 'from'):
            return index[1];            
    return [str(id)];  

#takes in item id and returns list of all items which eventually
#build into original item.
#returned data in format of:
# [[,],[item id, number of items bellow it in hierarchy],[,]]
def completeDecompItem(id):
    finalList = [];
    subList = [];
    offset =0;  #used to keep track of nesting
    component = decompItem(id);
    if(int(component[0]) != int(id)):  #if not base item
        for subItem in component:
            subList = completeDecompItem(subItem);
            offset =  len(subList);
            finalList.extend(completeDecompItem(subItem));
    finalList.append([str(id),len(component)+offset]);
    return finalList;


#take build and returns all items which are used to develop build
def decompBuild(Build):
    totalDecomp = [];
    for i in range(0,6):
        if(Build.getSlot(i) == 0):
            continue;
        if(Build.getSlot(i)[0]==0):
            continue;
        totalDecomp.extend(completeDecompItem(Build.getSlot(i)[0]));
    return totalDecomp;
   # print("-99");        

#takes list of items [[id,#sub items]]
#returns [[id, gold, #subitems]]
def decompAddGold(oldList):
    newList =[];
    for i in range(0,len(oldList)):
       # append 0=gold 1=item id 2=#of subitms
        newList.append([(oldList[i][0]), id2Gold(oldList[i][0]),oldList[i][1]]);
    return newList;    
#takes id returns gold    
def id2Gold(id):
    if(id == 0):
        id= 1052;  #FIX IN LONGTERM MODEL, THIS ACCOUNTS FOR 0 item
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['gold']['total'];    
    
#x = possibleBuild([3075,0,0],[1001,-9,-9],0,0,0,0,-9); #3047
x = possibleBuild([3075,-9,-9],0,0,0,0,0,0);

#print(buildChainCompatible(r,x));
#y = completeDecompItem(3075);

y = decompBuild(x);
z = decompAddGold(y); 
z.reverse();   #DONOT DELETe
print(z);

zz=determinePossibleBuildSequence(len(y), z);

for i in zz:
    print(i.profile());

chunks = chunkByInterval(zz);
print(chunks[2]);
bt = buildTrailer(x,chunks,2);

print(bt[0]);
#trail = buildTrailerLink(x, chunks, 2, [])
#print("trail", trail);


#print(trail[3][1].profile());
#print(id2Name(1031));
#print(id2Name(1029));