#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:59:43 2019

@author: robert
"""

import sys

valOne = ""
valTwo = ""
value = 0

hand = sys.stdin.readline().split()

for i in range(5):
    match = 1
    valOne = (hand[i])[0]
    for j in range(i + 1, 5):
        valTwo = (hand[j])[0]
        
        if valOne == valTwo:
            match = match + 1
            
    if match > value:
        value = match
        
print(value)