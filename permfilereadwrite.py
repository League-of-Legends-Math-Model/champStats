# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:00:45 2016

@author: Max

"""

import pickle;
import datetime;
from itempull import *;

gold = 14000;
fileDate = datetime.datetime.now();
#newFileBytes = [123, 3, 0, 100];
#ewFileByteArray = bytearray(newFileBytes);


detBuilds = determinePossibleBuildsFile(0,gold);

'''
newFile = open("permFiles/uh.txt", "wb");
p = pickle.Pickler(newFile);
p.dump(detBuilds);
'''
'''
fh = open('permFiles/perm40.txt', 'rb');
up = pickle.Unpickler(fh);
j = up.load();

ah = determinePossibleBuilds(400);
print(ah[0].profile());
print(j[0].profile());
'''
#print(fileDate);