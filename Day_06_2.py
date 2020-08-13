#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:28:24 2020

@author: venky

There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location  and moves at a rate of  meters per jump. The second kangaroo starts at location  and moves at a rate of  
meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they’ll ever land at the same location at the same time?

Input Format
A single line of four space-separated integers denoting the respective values of , , , and .
Constraints
Output Format
Print YES if they can land on the same location at the same time; otherwise, print NO.
Note: The two kangaroos must land at the same location after making the same number of jumps.
Sample Input 0
0 3 4 2
Sample Output 0
YES
Explanation 0
The two kangaroos jump through the following sequence of locations:
Thus, the kangaroos meet after  jumps and we print YES.
Sample Input 1
0 2 5 3
Sample Output 1
NO
Explanation 1
The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo’s starting location (i.e., ). Because the second kangaroo moves at a faster rate (meaning ) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

if __name__ == '__main__':
    x1, v1, x2, v2 = raw_input().strip().split(' ')
    x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
    result = kangaroo(x1, v1, x2, v2)
    print(result)
