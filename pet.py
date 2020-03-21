#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:49:51 2019

@author: robert
"""

import sys

highScore = 0
winner = 0

for i in range(1, 6):
    scores = sys.stdin.readline().split()
    totalScore = 0
    for j in range(4):
        totalScore = totalScore + int(scores[j])
        if highScore < totalScore:
            highScore = totalScore
            winner = i
print(str(winner) + " " + str(highScore)) 
    