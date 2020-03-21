#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:51:50 2019

@author: robert
"""

import sys

AI = sys.stdin.readline().split()

A = int(AI[0])
I = int(AI[1])

print(A * (I - 1) + 1)