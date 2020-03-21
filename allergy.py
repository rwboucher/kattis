#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:42:56 2019

@author: robert
"""

import sys

days = []

td = 0

numTests = int(sys.stdin.readline())

for num in range(numTests):
    days.append(int(sys.stdin.readline()))
    
days.sort(reverse = True)

i = 0
td = 0

if len(days) == 1:
    print(str(days[0]))
    sys.exit()

elif (i + 1) < len(days) and days[i] == days[i + 1]:
    td = (2 * days[i]) + len(days) - 3
    sys.exit()
    
elif (i + 3) > len(days):
    td = days[i] + 1
    sys.exit()
    
else:
    if days[0] == 5:
        middle = 5
        for j in range(1, len(days) - 1, 2):
            right = days[j]
        for k in range(2, len(days) - 1, 2):
            left = days[k]
print(td)
    
    
    