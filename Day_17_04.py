#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:14:03 2020
Sock Merchant
from collections  import    Counter
>> arr = [10 ,20, 20, 10, 10, 30, 50, 10, 20]
>>> Counter(arr)
Counter({10: 4, 20: 3, 50: 1, 30: 1})
>>> Counter(arr).values()
[4, 3, 1, 1]
>>> Counter(arr).keys()
[10, 20, 50, 30]

@author: venky
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s=0
    for val in Counter(ar).values():
        s+=val//2
    return s 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
