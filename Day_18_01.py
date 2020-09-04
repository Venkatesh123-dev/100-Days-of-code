#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:34:19 2020
Check Subset
@author: venky
"""
for _ in range(int(input())):
    a, A = input(), set(input().split())
    b, B = input(), set(input().split())

    print(A.issubset(B))
    
    
## Enter your code here. Read input from STDIN. Print output to STDOUT

def checker():
    x = int(input())
    s1 = set(map(int,input().split()))
    y = int(input())
    s2 = set(map(int,input().split()))
    l = []
    for i in s1:
        if i in s2:
            l.append(i)

    l = set(l)

    if l == s1:
        print("True")
    else:
        print("False")
        
        
t = int(input())
for i in range(t):
    checker()        
    