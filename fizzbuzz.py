#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:59:29 2019

@author: robert
"""

import sys

XYN = sys.stdin.readline().split()

X = int(XYN[0])
Y = int(XYN[1])
N = int(XYN[2])

for i in range(1, N + 1):
    if i % X == 0:
        if i % Y == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % Y == 0:
        print("Buzz")
    else:
        print(i)
            
    