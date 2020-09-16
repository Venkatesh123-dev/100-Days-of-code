#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:38:28 2020
Maximize It!
@author: venky
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
n,m = [ int(x) for x in input().split() ]
l1 = list()
for i in range(n):
    l = list(map(int, input().split()))[1:]
    l1.append(l)
res = map(lambda x: sum(i*i for  i in x)%m,product(*l1))
print(max(res))
    
