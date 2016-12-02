# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:00:45 2016

@author: Max
"""
import pickle;
import datetime;
goldPerm = 1000;
fileDate = datetime.datetime.now();
#newFileBytes = [123, 3, 0, 100];
#ewFileByteArray = bytearray(newFileBytes);
'''
gold = 1000
detBuilds = determinePossibleBuildsFile(gold)
newFile = open("uh.txt", "wb");
p = pickle.Pickler(newFile);
p.dump(detBuilds);
'''


fh = open('uh.txt', 'rb');
up = pickle.Unpickler(fh);
j = up.load();
print(j[60][6].profile());

    
#print(fileDate);