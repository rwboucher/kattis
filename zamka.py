#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:54:13 2019

@author: robert
"""

import sys

L = int(sys.stdin.readline())
D = int(sys.stdin.readline())
X = int(sys.stdin.readline())

max = int(L)
min = int(D)

for i in range(L, D + 1):
    total = 0
    for digit in str(i):
        total = total + int(digit)
    if total == int(X):
        if int(i) > max:
            max = int(i)

for i in range(D, L - 1, -1):
    total = 0
    for digit in str(i):
        total = total + int(digit)
    if total == int(X):
        if int(i) < min:
            min = int(i)

print(min)
print(max)
        