#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:08:53 2020
Hacker rank The Minion Game
@author: venky
"""
def minion_game(s):
    # your code goes here
    s1 = 0
    s2 = 0
    vow = "AEIOU"
    for  i in range(len(s)):
        if s[i]   in vow:
            s1 = s1+(len(s)-i)
        else:
            s2 = s2+(len(s)- i)

    if s1 > s2:
        print("Kevin",s1)
    elif s2 > s1:
        print("Stuart", s2)
        
    else:
        print("Draw")    


minion_game("BANANA")