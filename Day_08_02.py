#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:16:15 2020

@author: venky
"""
"""Write a program that accepts a string as an input and creates a dictionary that counts the number of times each letter is present in the string and is NOT case sensitive (i.e. 'Aa' would count as 2 a's). The keys should be the letters and the values should be the number of times that letter is in the string. For example an input of 'aabbcAa' would return {'a':4,'b':2,'c':1}. The alphabet string is already provided for you. (Hint: consider converting input string to lower case.)"""


"""

alphabet = 'aaabcdefghijklmnopqrstuvwxyz'
# Your code here
def char_frequency(alphabet):
    dict = {}
    for n  in alphabet:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency(alphabet))  """



alphabet = 'aabbccdefghijklmnopqrstuvwxyz'
# Your code here
from collections import Counter 
res = Counter(alphabet) 
print(res)




"""Write a Python function to sum the first N numbers starting with 0. So if N is 4 then your function should add 0 + 1 + 2 + 3"""

def sum_first_n(N):
    sum = 0
    for i in range(0,N+1):
        sum+= i
    return sum


print(sum_first_n(10))



n = 10
sum = 0
for num in range(0, n+1,1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )