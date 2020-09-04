#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:22:25 2020
No Idea!
@author: venky
"""


n, m = input().split()

array = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A) - (i in B) for i in array]))

#second approach
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = input().split()
happiness =0
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
for i in arr:
    if i  in  A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)        

