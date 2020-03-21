#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:06:17 2019

@author: robert
"""

import sys

numTestCases = sys.stdin.readline()
    
for testCase in sys.stdin:
    Cn1n5n10 = testCase.split()
    C = int(Cn1n5n10[0])
    n1 = int(Cn1n5n10[1])
    n5 = int(Cn1n5n10[2])
    n10 = int(Cn1n5n10[3])
    
    coinsUsed = 0

    numOf8 = C - n10 - n5
    
    if C * 8 > (10 * n10 + 5 * n5 + n1):
        coinsUsed = -1
        C = 0
    
    while C > 0:
        if n10 > 0 and numOf8 > 0:
            n10 = n10 - 1
            n1 = n1 - 3
            n5 = n5 + 1
            numOf8 = numOf8 - 1
            C = C - 1
            coinsUsed = coinsUsed + 4            
        elif n10 > 0:
            n10 = n10 - 1
            n1 = n1 + 2
            C = C - 1
            coinsUsed = coinsUsed + 1
            
        elif n5 >= (2 * C) or (n5 > 1 and n1 < 3):
            coinsUsed = coinsUsed + 2
            n5 = n5 - 2
            n1 = n1 + 2
            C = C - 1
            
        elif n5 > 0:
            n5 = n5 - 1
            n1 = n1 - 3
            coinsUsed = coinsUsed + 4
            C = C - 1
            
        else:
            coinsUsed = coinsUsed + (8 * C)
            C = 0
            
    print(coinsUsed)