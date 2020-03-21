#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:41:28 2019

@author: robert
"""

import sys

quantity = int(sys.stdin.readline())

for i in range(quantity):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")