#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:55:01 2020

@author: venky
"""
""" Dictionaries and Maps
Given n  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  name  is not found, print Not found"""


n = int(input())
d = dict()
for i in range(0,n):
    name,number = input().split()
    d[name] = number

for i  in range(0,n):
    name = input()
    if name in d:
        print("{}={}".format(name, d[name]))
    else:
        print("Not found")


"""
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument"""
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n)) """


def factorial(num):
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

factorial(4)        