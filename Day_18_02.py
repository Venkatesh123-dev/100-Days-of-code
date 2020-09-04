#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:49:28 2020
Check Strict Superset


@author: venky
"""
A = set(input().split())

for _ in range(int(input())):
    if not A.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)
    
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
def checker():
    sub = set(map(int,input().split()))
    if sub.issubset(a):
        if len(sub)==len(a):
            l.append(1)
        else:
            l.append(0)    
    else:
        l.append(0)

a = set(map(int, input().split()))
n = int(input())
l = []
for i in  range(n):
    checker()

if any(l)==l:
    print("True")
else:
    print("False")     