#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:26:22 2019

@author: robert
"""

import sys

testCases = int(sys.stdin.readline())

for i in range(testCases):
    citiesVisited = 0
    visitedList = []
    numVisits = int(sys.stdin.readline())
    for visit in range(numVisits):
        visitedList.append(sys.stdin.readline())
    citiesVisited = len(set(visitedList))
    print(citiesVisited)    
        
        