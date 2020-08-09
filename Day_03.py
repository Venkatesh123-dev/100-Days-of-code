#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:03:59 2020

@author: venky
"""

"""Python If-Else

Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2  to 5 , print Not Weird
If n is even and in the inclusive range of 6  to 20 , print Weird
If n is even and greater than 25 , print Not Weird"""




n  = int(input())
if n % 2 == 1:
    print(" Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print ("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print ("Not Weird")
