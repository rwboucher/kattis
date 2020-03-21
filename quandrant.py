#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:47:42 2019

@author: robert
"""
import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x > 0:
    if y > 0:
        print("1")
        sys.exit()
    else:
        print("4")
        sys.exit()
else:
    if y > 0:
        print("2")
        sys.exit()        
    else:
        print("3")
        sys.exit()
        