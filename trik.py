#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:04:25 2019

@author: robert
"""

import sys

cup = 1

moves = sys.stdin.readline()

for move in moves:
    if move == 'A':
        if cup == 1:
            cup = 2
        elif cup == 2:
            cup = 1
    elif move == 'B':
        if cup == 2:
            cup = 3
        elif cup == 3:
            cup = 2
    elif move == 'C':
        if cup == 3:
            cup = 1
        elif cup == 1:
            cup = 3
print(cup)