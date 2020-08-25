#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:48:32 2020

@author: venky
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i,num in enumerate(s):
        if sum(s[i:i+m]) == d:
            count += 1

    return count        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
#second  approach

n = int(input())

sq = [int(ele) for ele in input().split()]

d, m = [int(ele) for ele in input().split()]

res = 0

for i in range(0, n - m + 1):
#    print( sq[i : i + m] , ':' , sum(sq[i : i + m]) )
    if(sum(sq[i : i + m]) == d):
        res += 1

print(res)    
    