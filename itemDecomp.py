# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:41:19 2016

@author: Max
"""

from copy import copy, deepcopy;
import requests;
import pickle;
import json

def id2Name(id):
    if(id == 0):
        id= 1052;  #FIX IN LONGTERM MODEL, THIS ACCOUNTS FOR 0 item
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['name'];
    
def id2Into(id):
    if(id == 0):
        id= 1052;  #FIX IN LONGTERM MODEL, THIS ACCOUNTS FOR 0 item
    url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/"+str(id)+"?itemData=all&api_key=444a50cf-4457-4339-8f70-2369dbd09b18";
    itemResponse = requests.get(url);
    currentItem = itemResponse.json();   
    return currentItem['into'];

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

def completeDecompItem(id):
    finalList = [];
    component = decompItem(id);
    if(int(component[0]) != int(id)):  #if not base item
        for subItem in component:
            #finalList.append(str(subItem));
            finalList.extend(completeDecompItem(subItem));
    finalList.append(str(id));
    return finalList;

#def permDecompItem(subItems):

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


x = possibleBuild([3047,0,0],[3075,-9,-9],[1001,-9,-9],0,0,0,-9);
print(completeDecompItem(3047));
print(completeDecompItem(3075));
print(decompBuild(x));
'''
print(decompItem(3047));  
print(decompItem(1001));      
print(id2Name(3075));
print(id2Into(1031));
#print(completeDecompItem(1001));
print(completeDecompItem(3075));
'''