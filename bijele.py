#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:08:44 2019

@author: robert
"""

import sys

king = 1
queen = 1
rook = 2
bishop = 2
knight = 2
pawn = 8

KQRBKP = sys.stdin.readline().split()

king = king - int(KQRBKP[0])
queen = queen - int(KQRBKP[1])
rook = rook - int(KQRBKP[2])
bishop = bishop - int(KQRBKP[3])
knight = knight - int(KQRBKP[4])
pawn = pawn - int(KQRBKP[5])
print(str(king) + " " + str(queen) + " " + str(rook) + " " + str(bishop) + " " + str(knight) + " " + str(pawn))
