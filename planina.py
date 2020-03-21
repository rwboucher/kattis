#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:35:22 2019

@author: robert
"""

import sys

totalPoints = 0
pps = 2

numOfIts = int(sys.stdin.readline())

for i in range(numOfIts):
    totalPoints = (pps + pps - 1) ** 2
    pps = pps + pps - 1
    
print(totalPoints)