#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:53:41 2020

@author: venky
"""
"""Arrays,Print the elements of array A in reverse order as a single line of space-separated numbers."""


import math
import os
import random
import re
import sys


#method1
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in range(n-1,-1,-1):
        print(arr[i], end=" ")



#method2

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr.reverse()
    for num in arr:
        print(num,end = ' ')
