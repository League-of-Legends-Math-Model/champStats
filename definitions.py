# -*- coding: utf-8 -*-
"""
Created on Tue May  9 01:28:18 2017

@author: Jon-Michael
"""

from copy import copy, deepcopy
import numpy as np

def findMean(a):
    length = len(a)
    mean = deepcopy(a[0])
    for i in range(1, length):
        mean += a[i]
    for i in range(0, len(mean)):
        mean[i] = mean[i] / length
    return mean

def computeSigma(mean, a):
    length = len(a)
    size = len(a[0])
    sigma = np.zeros(shape = (size, size))
    for i in range(0, length):
        diff = np.zeros(shape = (size, 1))        
        for j in range(0, size):
            diff[j] = a[i][j] - mean[j]

        for j in range(0, size):
            for k in range(0, size):
                sigma[i][j] += diff[i]*diff[j]
    for i in range(0, size):
        for j in range(0, size):
            sigma[i][j] = sigma[i][j] / length
    return sigma

        