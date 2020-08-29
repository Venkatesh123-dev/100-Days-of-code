#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:51:46 2020

@author: venky
"""
"""Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line."""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = neg = zero = 0

    for i in range(n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1

    print(pos/n)
    print(neg/n)
    print(zero/n)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
"""

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    neu=0
    for i in range(len(arr)):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]==0):
            neu+=1
        else:
            neg+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(neu/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr) """