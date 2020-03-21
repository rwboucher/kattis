#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:07:41 2019

@author: robert
"""

import sys

for line in sys.stdin:
    for i in range(len(line) - 2):
        if line[i] == 's' and line[i + 1] == 's':
            print("hiss")
            sys.exit()
    print("no hiss")
    sys.exit()