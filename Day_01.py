#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:54:31 2020

@author: venky
"""

#Reverse the sentence
"""
Write a program to reverse the sentence wordwise.

Input:
You have entered a wrong domain
Output:
domain wrong a entered have You  """


#import pdb;pdb.set_trace()
val=raw_input("Please enter a sentence:")
#write down your logic here

word = val.split()
words = list(reversed(word))
reversed = ' '.join(words)
print(reversed)


