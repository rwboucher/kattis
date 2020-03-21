#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:12:03 2019

@author: robert
"""

import sys

planMB = int(sys.stdin.readline())
numMonths = int(sys.stdin.readline())
totalAvailable = 0
monthlyLeftover = 0
totalLeftover = 0

for month in sys.stdin:
    usedMB = int(month)
    monthlyLeftover = planMB - usedMB
    totalLeftover = totalLeftover + monthlyLeftover
    
totalAvailable = totalLeftover + planMB

print(totalAvailable)
    
    
