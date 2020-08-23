#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:22:54 2020

@author: venky
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mincount = maxcount = 0
    minscore = maxscore = scores[0]

    for i in range(1,len(scores)):
        if minscore < scores[i]:
            minscore = scores[i]
            mincount += 1

        elif maxscore > scores[i]:
            maxscore = scores[i]
            maxcount += 1
            
    return mincount,maxcount        

scores = [10,5,20,20,4,5,2,25,1]
print(breakingRecords(scores))

  