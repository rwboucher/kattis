#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:50:56 2019

@author: robert
"""

import sys

wipes = int(sys.stdin.readline())
input = sys.stdin.readline()
flipInput = ""
for i in range(len(input) - 1):
    orig = int(input[i].strip())
    flip = abs(orig - 1)
    flipInput = flipInput + str(flip)
output = sys.stdin.readline()
if wipes % 2 == 0:
    if output == input:
        print("Deletion succeeded")
        sys.exit()
else:
    if output.strip() == flipInput.strip():
        print("Deletion succeeded")
        sys.exit()
print("Deletion failed")
            
        