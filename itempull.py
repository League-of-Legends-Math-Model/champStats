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
numberOfItemsInBank =0;
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
    def reposition(self):
        #print(self.slot[0][2] < self.slot[1][2]);'''
        for i in range(0,6-self.open):
            for j in range(i+1,6-self.open):
                if(self.slot[j][2]>self.slot[i][2]):
                    temp = self.slot[j];
                    self.slot[j]=self.slot[i];
                    self.slot[i]=temp;
#'''                    
        return self;
        ##construct a new build by adding a new item
    def newBuild(self,newItem,oldBuild):
        #find open slot
        if(oldBuild.getOpenSlots()==0):
            print("Your out of room");
        if(oldBuild.getOpenSlots()==1):
            return possibleBuild(oldBuild.getSlot(0),
            oldBuild.getSlot(1),
            oldBuild.getSlot(2),
            oldBuild.getSlot(3),
            oldBuild.getSlot(4),
            newItem,
            oldBuild.getGold()).reposition();
        if(oldBuild.getOpenSlots()==2):
            return possibleBuild(oldBuild.getSlot(0),
            oldBuild.getSlot(1),
            oldBuild.getSlot(2),
            oldBuild.getSlot(3),
            newItem,
            0,
            oldBuild.getGold()).reposition();
        if(oldBuild.getOpenSlots()==3):
            return possibleBuild(oldBuild.getSlot(0),
            oldBuild.getSlot(1),
            oldBuild.getSlot(2),
            newItem,
            0,
            0,
            oldBuild.getGold()).reposition();
        if(oldBuild.getOpenSlots()==4):
            return possibleBuild(oldBuild.getSlot(0),
            oldBuild.getSlot(1),
            newItem,
            0,
            0,
            0,
            oldBuild.getGold()).reposition();
        if(oldBuild.getOpenSlots()==5):
            return possibleBuild(oldBuild.getSlot(0),
            newItem,
            0,
            0,
            0,
            0,
            oldBuild.getGold()).reposition();
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
        return "items:"+str(self.slot[0])+","+str(self.slot[1])+","+str(self.slot[2])+","+str(self.slot[3])+ ","+str(self.slot[4])+","+str(self.slot[5])+"remG:"+str(self.remG)+"open:"+str(self.open);
    def getOpenSlots(self):
        return self.open;
        


    
#TODO dynamic programming algorithm
 
s=[]; #item combos with i *10 gold
def determinePossibleBuilds(gold):
    global s;
    s=[];
    for permIndex in range(0,gold):
        print(permIndex);
       # if(permIndex != 0):
           # print(permIndex-1,":",s[permIndex-1]);
        #for every item that cost less than permIndex*100 gold
        s.append([]);
        currentGold  = permIndex*10;
        for newItem in canAfford(currentGold):
            #newItems gold
            remainingGold = currentGold-newItem.getSlot(0)[2];#subtract cost of item
            permGroup = s[int(remainingGold/10)];
            #add builds of new item and lower s to the new s
            s[permIndex].extend(adjoinItemToPermGroup(permGroup,newItem.getSlot(0),remainingGold));
            
#given an item and a group of potential builds return an array
# of new builds which attach the item to each build in permgroup
adjoinedItems = [];
adjoinedItemsSize =0;
def adjoinItemToPermGroup(permGroup, item, remainingGold):
    global adjoinedItems;
    global adjoinedItemsSize;
    adjoinedItems = [];
    adjoinedItemsSize=0;
   # print("n:",n,"pg:",permGroup);
    #if its empty
    #if (len(permGroup) == 0):
        #TODO FIX GOLD
    adjoinedItems.append(possibleBuild(item,0,0,0,0,0,remainingGold)); #add just the item
    for key in permGroup:
        #exclude perms with all slots fileld        
        if(key.getOpenSlots()>0):
            adjoinedItems.append(key.newBuild(item, key));
            adjoinedItemsSize= adjoinedItemsSize+1;
    return adjoinedItems;
           
#returns array of possible items to be purchased with remaining gold           
#affordable=[-9 for x in range(300)];      
affordable=[]
affordableSize =0;
def canAfford(gold):
    global affordable;
    affordable=[];
    index =0;
    for i in range(0, numberOfItemsInBank):
       if(itemBank[i][2]<=gold):
           #affordable[index] = possibleBuild(itemBank[i],0,0,0,0,0,(gold - itemBank[i][2]));
           index= index+1;
           affordable.append(possibleBuild(itemBank[i],0,0,0,0,0, (gold - itemBank[i][2])));
    global affordableSize;
    affordableSize = index;
    return affordable;
           
generateItemBank()

determinePossibleBuilds(101);

'''
print("Permutations for 150 gold")
for i in s[40]:
    print(i.profile());
  '''
print(len(s[100]));
print("ITEMS TO PERMUTe");
po = canAfford(1000)
for i in po:
    print(i.profile());