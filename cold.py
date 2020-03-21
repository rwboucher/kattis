#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:57:19 2019

@author: robert
"""

import sys

lessThanZero = 0

numTemps = int(sys.stdin.readline())
temps = sys.stdin.readline().split()

for temp in temps:
    temp = int(temp)
    if temp < 0:
        lessThanZero = lessThanZero + 1
        
print(lessThanZero)    