# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:17:19 2016

@author: Max Highsmith

Given two champions this estimates who will win.
"""
import numpy as np;

#Champion applies move
def takeTurn(move,target, moveChampStats, targetChampStats):
#is a physical attack
    if (True):
        return (target - (move*(100/(100+targetChampStats[4]))));   #factor in armor etc
        

def battleDamadge(champ1BattleMatrix, champ2BattleMatrix,  champ1Stats, champ2Stats):


#name arrays
    Champ1MoveArray=champ1BattleMatrix[1];
    Champ1TimeStampArray=champ1BattleMatrix[0];
    Champ2MoveArray=champ2BattleMatrix[1];
    Champ2TimeStampArray=champ2BattleMatrix[0];
#Set Champions health    
    HealthChamp1 = champ1Stats[0];  #
    HealthChamp2 = champ2Stats[0];   #TBD
    
    timeBank1=0;
    timeBank2=0;
    index1=0;
    index2=0;
    for i in range(1,100):
        timeBank1 = timeBank1+1;
        timeBank2 = timeBank2+1;
        #if enough time has passed for champ1 to use move
        if(Champ1TimeStampArray[index1]<timeBank1):   # check if the move has been channeled long enough
            timeBank1=0;  # mark time as used
            HealthChamp2 = takeTurn(Champ1MoveArray[index1], HealthChamp2,champ1Stats, champ2Stats);
            index1 = index1 +1;
        #if enough time has passed for champ2 to use move
        if(Champ2TimeStampArray[index2]<timeBank2):
            timeBank2=0; 
            HealthChamp1 = takeTurn(Champ2MoveArray[index2], HealthChamp1,champ2Stats, champ1Stats);
            index2 = index2 +1;
            
        print(index1, index2, HealthChamp1, HealthChamp2);    
        #Check if either champ is dead        
        if(HealthChamp1 <= 0):
            print("champ1 dead");
            break;
        if(HealthChamp2 <= 0):
            print("champ2 dead");
            break;
            
champ1time = [2   ,2  ,2  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ];
champ2time = [3   ,2  ,2  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ];
champ1Move = [50  ,50 ,50 ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ];
champ2Move = [50 ,50 ,50 ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ,40  ];
champ1BattleMatrix = np.stack((champ1time, champ1Move),0);
champ2BattleMatrix = np.stack((champ2time, champ2Move),0);
champ1stats = [100,1,1,1,1,1,1,1];
champ2stats = [100,1,1,1,1,1,1,1];
print(champ1BattleMatrix[0]);
battleDamadge(champ1BattleMatrix, champ2BattleMatrix, champ1stats, champ2stats);
#battleDamadge(champ1Move, champ1time, champ2Move, champ2time);