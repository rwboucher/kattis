#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:06:26 2019

@author: robert
"""

import sys

tests = int(sys.stdin.readline())

for test in range(tests):
    rec = sys.stdin.readline().split()
    r = int(rec[0])
    e = int(rec[1])
    c = int(rec[2])
    
    if r > (e - c):
        print("do not advertise")
    elif r < (e - c):
        print("advertise")
    else:
        print("does not matter")
    