#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:53:49 2019

@author: robert

w = lenght of wire
d = distance between birds
n = current number of birds
b = additional birds
e = empty
o = occupied
"""

import sys

wdn = sys.stdin.readline().split()
w = int(wdn[0])
d = int(wdn[1])
n = int(wdn[2])

ab = 0

if w < 12:
    print(ab)
    sys.exit()
    
birds = ['e'] * w

for bird in range(n):
    loc = int(sys.stdin.readline())
    birds[loc] = 'o'

for i in range(6, (w - 6) + 1):
    if birds[i] != 'o':
        for j in range(d):
            if ((i - j) > 0 and birds[i - j] == 'o') or ((i + j) < w and birds[i + j] == 'o'):
                add = 0
                break
            else:
                print(str(i) + "" + str(birds[i]))
                birds[i] = 'o'
                add = 1
        ab = ab + add
        
print(ab)

#for i in range(w):
 #   print(birds[i])
    

