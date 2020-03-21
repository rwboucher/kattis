#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:15:17 2019

@author: robert
"""

import sys

bases = 0
rab = 0

numAtBats = sys.stdin.readline()

atBats = sys.stdin.readline().split()

for atBat in atBats:
    atBat = float(atBat)
    if atBat >= 0:
        rab = rab + 1
        bases = bases + atBat

print(bases/rab)