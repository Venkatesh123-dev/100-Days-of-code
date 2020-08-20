#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:21:13 2020

@author: venky
"""
"""Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number."""


array = [9,6,7,4,2,1]


def getSubarrayWithSum(arr,s):
    result = []
    for x  in range(len(arr)):
        result.append(arr[x])
        while (sum(result) > s):
            result.pop(0)
        if (sum(result) == s):
            return result
    return []

print(getSubarrayWithSum(array,22))
