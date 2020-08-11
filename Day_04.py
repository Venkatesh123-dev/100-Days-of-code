#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:39:17 2020
factorila  with  recursion  and  without recursion
@author: venky
"""

tests = [3,4, 8, 10, 12, 100]

def fact(x):
    if x > -1:
        if x == 0:
            return 1
        else:
            return  x * fact(x-1)
        
    else:
        return "Negative"
    
    


for test in tests:
    print(fact(test))    
    
    
def  fact(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    print(total)    
   
#fact(4)


for test in tests:
    fact(test)    
    

   