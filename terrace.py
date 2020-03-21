#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:31:08 2019

@author: robert
"""

import sys

denied = 0
terrace = 0

Lx = sys.stdin.readline().split()

L = int(Lx[0])
x = int(Lx[1])

for e in range(x):
    eventp = sys.stdin.readline().split()
    event = eventp[0]
    p = int(eventp[1])
    if event == "leave":
        terrace = terrace - p
    elif (terrace + p) < L:
        terrace = terrace + p
    else:
        denied = denied + 1
        
print(denied)
        
        