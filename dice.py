#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:27:32 2019

@author: robert
"""

import sys

NM = sys.stdin.readline().split()

N = int(NM[0])
M = int(NM[1])

total = N + M

totals = [None] * (total + 1)

for i in range(total + 1):
    totals[i] = 0

for j in range(1, N + 1):
    for k in range(1, M + 1):
        roll = j + k
        totals[j + k] = totals[j + k] + 1
        
highest = max(totals)

for i in range(total + 1):
    if totals[i] == highest:
        print(i)



