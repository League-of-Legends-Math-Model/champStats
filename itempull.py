# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:48:55 2016

@author: Max
"""
import requests
import json

##generates 3d array of items by traversing json data
#0 -item Id
#1 -item Name
#2 -item gold
#shop items is global
url="https://global.api.pvp.net/api/lol/static-data/na/v1.2/item?itemListData=gold&api_key=444a50cf-4457-4339-8f70-2369dbd09b18"
response = requests.get(url);
itemList = response.json();    
itemBank =[[0 for x in range(3)] for y in range(len(itemList['data']))];
numberOfItemsInBank;
print("item list length%n",len(itemList['data']));
def generateItemBank():
    global numberOfItemsInBank;
    index = 0;
    for key in itemList['data']:
        try:
            #print(itemList['data'][key]['name']);
            if(itemList['data'][key]['gold']['purchasable'] == True and
            itemList['data'][key]['gold']['total']!= 0):  #skips items that cannot be purchased, 0gold items
                itemBank[index][0]= itemList['data'][key]['id'];
                itemBank[index][1]= itemList['data'][key]['name'];
                itemBank[index][2]= itemList['data'][key]['gold']['total'];
                index=index+1;
                numberOfItemsInBank = index;
        except KeyError:   #riot has some id items without names or cost...
            print("oophsy doopsy no name here");   
    return 1;
def swapItem(x,y):
    tempcode= x[0];
    tempode = x[1];
    tempgold = x[2];
    x[0]=y[0];
    x[1]=y[1];
    x[2]=y[2];
    y[0]=tempcode;
    y[1]=tempode;
    y[2]=tempgold;
   #sort item bank according to Item 
def quickSortItems(bank,lo,hi):
    if(lo < hi):
        p = partitionItems(bank,lo,hi);
        quickSortItems(bank,lo,p-1);
        quickSortItems(bank,p+1,hi);
        
def partitionItems(bank, lo, hi):
    pivot = bank[hi][2];
    i = lo; #swap point
    for j in range(lo,hi-1):
        if(bank[j][2]<= pivot):
            swapItem(bank[i],bank[j]);
            i= i+1;
    swapItem(bank[i],bank[hi])
    return i;
   
############################33333
    ##simplified
#####
coins = [[0 for x in range(2)] for y in range(5)];
coins[0][0]='a';
coins[0][1]=2;
coins[1][0]='b';
coins[1][1]=3;
coins[2][0]='c';
coins[2][1]=2;
coins[3][0]='d';
coins[3][1]=5;
coins[4][0]='e';
coins[4][1]=4;

# 6 slots meant to contain id of item indexed from 0 to 5
#remG = remaining Gold
class possibleBuild(object):
    def __init__(self,i1,i2,i3,i4,i5,i6,remG):
        self.open=0;
        self.slot = [-9 for x in range(6)];
        self.slot[0]=i1;
        self.slot[1]=i2;
        self.slot[2]=i3;
        self.slot[3]=i4;
        self.slot[4]=i5;
        self.slot[5]=i6;
        self.remG = remG;
        self.calcSlotsOpen();
    def calcSlotsOpen(self):
        self.open =0;
        for i in range(0,6):
            if(self.slot[i] ==0):
                self.open= self.open +1;   
    def getSlot(self,i):
        return self.slot[i];
    def setSlot(self,i, x):
        self.slot[i] = x;
    def subGold(self, sub):
        self.remG = (self.remG - sub);
        return self.remG;
    def getGold(self):
        return self.remG;
    def profile(self):
        return "items:"+str(self.slot[0])+"remG:"+str(self.remG)+"open:"+str(self.open);
    def getOpenSlots():
        return self.open;
        
def coinPermutations():
    for permLevel in range(0,10):  #cycle through permutation groups
        for shopIndex in coins:
            if(shopIndex[1]<permLevel):# if coin can be afforded
                print("ok");
############################3333
##simpliciation
###################333333

#rearrange shopItems according to gold
def sortShopItems():
    return -99;
    
#TODO dynamic programming algorithm
s=[0 for x in range(100)]; #item combos with i *10 gold
def determinePossibleBuilds(gold):
    for i in range(0,100):
        currentPerms = [];
        if canAfford(i):
            print -99
    print -99;
           
#returns array of possible items to be purchased with remaining gold           
affordable=[-9 for x in range(300)];      
affordableSize =0;
def canAfford(gold):
    index =0;
    for i in range(0, numberOfItemsInBank):
       if(itemBank[i][2]<gold):
           global affordable;
           affordable[index] = possibleBuild(itemBank[i],0,0,0,0,0,(gold - itemBank[i][2]));
           index= index+1;
           #affordable.append(possibleBuild(itemBank[i],0,0,0,0,0, (gold - itemBank[i][2])));
    global affordableSize;
    affordableSize = index;
           
           
generateItemBank()

#for i in range(0, 9223372036854775807):
 #   print(i);

#for i in range(0,numberOfItemsInBank):
 #   print(itemBank[i]);
#bb = [];
#bb.append(possibleBuild(1,2,3,4,5,6,100));
#print(bb[0].getSlot(0));
canAfford(4000);
#for i in range(0, affordableSize):
 #   print(affordable[i].profile());
#coinPermutations();
quickSortItems(itemBank,0,numberOfItemsInBank);
for i in range(0,numberOfItemsInBank):
    print(itemBank[i]);
print(numberOfItemsInBank)
