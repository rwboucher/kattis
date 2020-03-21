#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:58:55 2019

@author: robert
"""

numPeriods = int(input())
qualInPeriod = 0
yearsInPeriod = 0
totalQuality = 0

for period in range(numPeriods):
    data = input().split(" ")
    qualInPeriod = float(data[0])
    yearsInPeriod = float(data[1])
    totalQuality = totalQuality + (qualInPeriod * yearsInPeriod)
    
print(totalQuality)   