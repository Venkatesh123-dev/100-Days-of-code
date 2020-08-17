#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:43:28 2020

@author: venky
"""
#Text Wrap

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


    
print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4))    
    

#Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    n = size
    l1 =  list(map(chr,range(97,123)))
    x = l1[n-1::-1]+l1[1:n]
    m = len("-".join(x))
    for i in range(1,n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))    

print_rangoli(5)

#output

"""

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
