#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:47:40 2019

@author: robert
"""

import sys

minRatio = 1

numberOfBalloons = int(sys.stdin.readline())

cannisters = sys.stdin.readline().split()

cannisters = [float(i) for i in cannisters]

cannisters.sort()

while numberOfBalloons > 0:
    
    if numberOfBalloons < cannisters[numberOfBalloons - 1]:
        print("impossible")
        sys.exit()
    else:
        ratio = cannisters[numberOfBalloons - 1]/numberOfBalloons
        if ratio < minRatio:
            minRatio = ratio
            
        numberOfBalloons = numberOfBalloons - 1

print(minRatio)
        
        
