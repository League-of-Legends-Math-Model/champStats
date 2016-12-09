# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:59:23 2016

@author: Max
"""

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
 