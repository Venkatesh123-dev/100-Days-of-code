#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:17:16 2020

@author: venky
"""
"""Pythagoras theorem
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2. a, b & c can be any element it's not necessary to be in sequence only."""


from itertools import combinations


def p_triplet(array):
    squared_num = dict((num**2, num) for num in array)

    triplet = [(squared_num[x],squared_num[y],squared_num[x+y]) for x,y in combinations(squared_num,2) if x+y in squared_num.keys()]
    #return triplet

    if triplet:
        print("Yes")
    else:
        print("No")
    




p_triplet([1,2,3,4,5,6,7,8,9])