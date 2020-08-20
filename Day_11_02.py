#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:24:28 2020

@author: venky
"""
"""You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template."""



def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap



print(is_leap(2020))


def  is_leap(year):
    leap = False
    if (year %4 ==0) and (year %100!=0  or year %400 == 0):
        leap = True
     
    return leap    
    

print(is_leap(1990))
    