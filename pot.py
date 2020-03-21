#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:00:17 2019

@author: robert
"""

import sys

total = 0

numAddends = sys.stdin.readline()

for addend in sys.stdin:
    base = int(addend.strip()[:-1])
    power = int(addend.strip()[-1:])
    expValue = base ** power
    total = total + expValue
    
print(total)