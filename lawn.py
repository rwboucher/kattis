#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:12:57 2019

@author: robert
"""

import sys

totalCost = 0.0

cost = sys.stdin.readline()
cpms = float(cost)
numLawns = int(sys.stdin.readline())
for lawn in sys.stdin:
    wl = lawn.split()
    w = float(wl[0])
    l = float(wl[1])
    cfl = w * l * cpms
    totalCost = totalCost + cfl
    
print(totalCost)   
    
    