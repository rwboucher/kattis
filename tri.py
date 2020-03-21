#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 06:36:03 2019

@author: robert
"""

import sys

ops = ['+', '-', '*', '/']
formula = ""

nums = sys.stdin.readline().split()

num1 = int(nums[0])
num2 = int(nums[1])
num3 = int(nums[2])

for op in ops:
    try:
        if eval(str(num1) + " " + op + " " + str(num2)) == num3:
            print(str(num1) + "" + op + "" + str(num2) + "=" + str(num3))
            sys.exit()
      
        elif eval(str(num2) + " " + op + " " + str(num3)) == num1:
            print(str(num1) + "=" + str(num2) + "" + op + "" + str(num3))
            sys.exit()
    except ZeroDivisionError:
        pass
        

