#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:14:01 2019

@author: robert
"""

import sys
import math

tests = int(sys.stdin.readline())

for test in range(tests):
    data = sys.stdin.readline().split()
    vel = float(data[0])
    ang = float(data[1])
    dis = float(data[2])
    bot = float(data[3])
    top = float(data[4])
        
    time = dis/(vel * math.cos(math.radians(ang)))
        
    y = vel * time * math.sin(math.radians(ang)) - 0.5 * (9.81 * (time ** 2))
        
    if (bot + 1) < y and (top - 1) > y:
        print("Safe")
    else:
        print("Not Safe")
    
    