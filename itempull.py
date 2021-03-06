# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:48:55 2016

@author: Max
"""
import requests;
import pickle;
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
#print("item list length%n",len(itemList['data']));


##DO NOT DELETE THIS IS AN ALTERNATIVE THAT GENERATES ENTIRE ITEM BANK.  WILL 
#BE USED WHEN WE EXTEND BEYOND ADC

"""
def generateItemBank():
    global numberOfItemsInBank;
    index = 0;
    for key in itemList['data']:
        try:
            #print(itemList['data'][key]['name']);
            #skips items that cannot be purchased, 0gold items
            if(itemList['data'][key]['gold']['purchasable'] == True and
            itemList['data'][key]['gold']['total']!= 0):  
                itemBank[index][0]= itemList['data'][key]['id'];
                itemBank[index][1]= itemList['data'][key]['name'];
                itemBank[index][2]= itemList['data'][key]['gold']['total'];
                index=index+1;
                numberOfItemsInBank = index;
        except KeyError:   #riot has some id items without names or cost...
            print("oophsy doopsy no name here");   
    return 1;
"""

###DONOT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#returns true if name matches the name of an Item we want to include
'''
1028 ruby crystal
1037 pickaxe
1038 b.f.sword
3101 stinger
3044 phage


'''

def isDesiredItem(id):
    if(
    id == 1018 or # cloak of agility
    id == 1027 or # saphire crystal
    id == 1028 or  #ruby crystal
    id == 1036 or  #long sword
    id == 1037 or    #pickaxe
    id == 1038 or     # b.f. sword
    id == 1042 or ##dagger
    id == 1043 or     #recursive bow
    id == 1051 or ## brawlers gloves
    id == 1053 or #vampire scepter
    id == 2015 or #kshard
    id == 3101 or    # stinger
    id == 3133 or  #caulefield warhammer
    id == 3031 or #infinty edge                         todo  250% crit
    id == 3034 or   #giant slayer                        
    id == 3035 or   #last whisper
    id == 3036 or  #Lord D regards
    id == 3044 or  #phage
    id == 3046 or  #phantom dancer
    id == 3057 or  ##sheen
    id == 3072 or #the blood thirstie
    id == 3078 or #trinty force
    id == 3085 or #runnans hurricaine
    id == 3086 or # recursive bow
    id == 3094 or #rapid fire cannn
    id == 3086 or #static shiv
    id == 3508):#ess reav       
        return True;
def generateItemBank():
    global numberOfItemsInBank;
    index = 0;
    for key in itemList['data']:
        try:
            #print(itemList['data'][key]['id']);
            #skips items that cannot be purchased, 0gold items
            if(isDesiredItem(itemList['data'][key]['id'])):  
                itemBank[index][0]= itemList['data'][key]['id'];
                itemBank[index][1]= itemList['data'][key]['name'];
                itemBank[index][2]= itemList['data'][key]['gold']['total'];
                index=index+1;
                numberOfItemsInBank = index;
        except KeyError:   #riot has some id items without names or cost...
            print("oophsy doopsy no name here");   
    return 1;   

##exhange two items  
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

#used to sort item bank
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
    
    
# The build object is a single instance of a feasible build which a champion 
#might be wearing.  There are 6 slots for the items slots,
#the RemG variable is used to identify the remaining gold that a champion
#would have if they were wearing the items identified in slot.
#Remg is dependent on the permutation group(the amount of money started with)
#Remg= (money to spend)- (money spent on items)
#open= the number of available slots

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
    
    #sort the build in descending value based on slot
    #the most expensive item will be slot 0
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
    def getItems(self):
        x =[];
        for i in range(0,6):
            if(self.slot[i] != 0):
                x.append(self.slot[i][0]);
            else:
                x.append(0);
        return x;
    #string display of build contents
    def profile(self):
        return ("items:"+str(self.slot[0])+","+str(self.slot[1])+","+
            str(self.slot[2])+","+str(self.slot[3])+ ","+str(self.slot[4])+","+
            str(self.slot[5])+"remG:"+str(self.remG)+"open:"+str(self.open));
    def getOpenSlots(self):
        return self.open;
        




s=[]; #item combos with i *10 gold
def determinePossibleBuildsFile(start,ggold):
    gold = int(ggold/10);
    global s;
    s=[];
    for permIndex in range(start,gold):
 #       print(permIndex);
       # if(permIndex != 0):
           # print(permIndex-1,":",s[permIndex-1]);
        #for every item that cost less than permIndex*100 gold
        s.append([]);
        currentGold  = permIndex*10;
        for newItem in canAfford(currentGold):
            #newItems gold
            #subtract cost of item
            remainingGold = currentGold-newItem.getSlot(0)[2];
            permGroup = s[int(remainingGold/10)];
            #add builds of new item and lower s to the new s
            s[permIndex].extend(adjoinItemToPermGroup(permGroup,
newItem.getSlot(0),remainingGold));
        newFile = open("permFiles/perm"+str(permIndex)+"0.txt", "wb");
        p = pickle.Pickler(newFile);
        p.dump(s[permIndex]);
        newFile.close();

    return s;
    
"""
DeterminePossibleBuilds is a dynamic programming algorithm which generates 
all possible builds given a specific amount of money. 

 It does this by 
dynamically constructing an array 's' of permutations
s[i] contains all possible permutations for (i*10) gold  (*10 for saving time)
permutations are arrays of possibleBuildObjects

"""
s=[]; #item combos with i *10 gold
def determinePossibleBuilds(ggold):
    gold = int(ggold/10);
    global s;
    s=[];
    for permIndex in range(0,gold):
  #      print(permIndex);
       # if(permIndex != 0):
           # print(permIndex-1,":",s[permIndex-1]);
        #for every item that cost less than permIndex*100 gold
        s.append([]);
        currentGold  = permIndex*10;
        for newItem in canAfford(currentGold):
            #newItems gold
            #subtract cost of item
            remainingGold = currentGold-newItem.getSlot(0)[2];
            permGroup = s[int(remainingGold/10)];
            #add builds of new item and lower s to the new s
            s[permIndex].extend(adjoinItemToPermGroup(permGroup,
newItem.getSlot(0),remainingGold));
    return s[gold-1];
            
"""
takes a permutations group and adds item to each build 
within the permutation
"""
adjoinedItems = [];
adjoinedItemsSize =0;
def adjoinItemToPermGroup(permGroup, item, remainingGold):
    global adjoinedItems;
    global adjoinedItemsSize;
    adjoinedItems = [];
    adjoinedItemsSize=0;
    #add just the item
    adjoinedItems.append(possibleBuild(item,0,0,0,0,0,remainingGold));
    for key in permGroup:
        #exclude perms with all slots fileld        
        if(key.getOpenSlots()>0):
            adjoinedItems.append(key.newBuild(item, key));
            adjoinedItemsSize= adjoinedItemsSize+1;
    return adjoinedItems;
           
           
           
           
"""returns array of possible items which could be purchased with a given
amount of gold           
"""   
affordable=[]
affordableSize =0;
def canAfford(gold):
    global affordable;
    affordable=[];
    index =0;
    for i in range(0, numberOfItemsInBank):
       if(itemBank[i][2]<=gold):
           index= index+1;
           affordable.append(possibleBuild(itemBank[i],0,0,0,0,0,
                                           (gold - itemBank[i][2])));
    global affordableSize;
    affordableSize = index;
    return affordable;
           
           
           
           
           
""""MAIN PROGRAM"""
#make the bank of items
generateItemBank()  

#generate array of permutations of builds up to index 100
#determinePossibleBuilds(1000);  #2100
#print(len(determinePossibleBuilds(1000)));
#print("perms",len(s[9]));
#print(s[90][3].getItems());
"""
#show permutations of 25 gold
dispNum = 100;
print("Permutations for",dispNum,"0");
for i in s[dispNum]:
    print(i.profile());

###displays number of posisble builds for 10000  
#(768266 if all purchasable items included)
print("number of permutaitons");
print(len(s[200]));

###displays all items which appear in permutations
print("ITEMS TO PERMUTe");
po = canAfford(3000)
for i in po:
    print(i.profile());
    '''

for i in range(0,numberOfItemsInBank):
    print (itemBank[i]);
    
    """