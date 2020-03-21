#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:01:07 2019

@author: robert
"""

import math

data = input().split(" ")
numMatches = int(data[0])
width = int(data[1])
height = int(data[2])
diagonal = math.sqrt(width ** 2 + height ** 2)

for match in range(numMatches):
    if int(input()) <= diagonal:
        print("DA")
    else:
        print("NE")