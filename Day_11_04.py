#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:41:13 2020

@author: venky

""A Very Big Sum

Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum +=ar[i]
    return sum


print(aVeryBigSum(ar=[5,1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

"""loops, Read an integer N . For all non-negative integers i < N , print i^2 . See the sample for details. """






if __name__ == '__main__':
    n = int(input("Please enter a number"))
    
    


for i in range(n+1):
    print (i**2)


"""Read an integer .
Without using any string methods, try to print the following:
Note that "" represents the values in between.
Input Format
The first line contains an integer .
Output Format
Output the answer as explained in the task


from __future__ import print_function



n = int(input())
for n in range(1,n+1):
    print(n,end = '') """




n = int(input("please  enter a number"))
for i in range(1,n+1):
    print(str(i),end = ' ')    


"""Loops"""
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Please enter a number"))
    

for i  in range(1,11):
    print(str(n) + " x " + str(i) + " = " + str(n * i))
