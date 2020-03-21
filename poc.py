#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:46:03 2019

@author: robert
"""

height = 4

data = list(map(int,input().split()))

side = data[0]
hcut = data[1]
vcut = data[2]

if(hcut >= side/2):
    width = hcut
else:
    width = side - hcut
    
if(vcut >= side/2):
    length = vcut
else:
    length = side - vcut
    
volume = length * width * height

print(volume)
