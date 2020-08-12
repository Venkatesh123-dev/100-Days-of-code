#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:10:20 2020
Python code to demonstrate example of variable scopes
@author: venky
"""

# Python code to demonstrate example 
# of variable scopes

# global variable
a = 100

# defining a function to test scopes
def func():
    # local variable
    b = 200

    # printing the value of global variable (a)
    # and, local variable (b)
    print("a: ", a, "b: ", b)
    
# main code
if __name__ == '__main__':
    # local variable of main
    c = 200
    
    # printing values of a, b and c
    print("a: ", a) #global 
    # print("a: ", b) #local of text *** will give an error
    print("c: ", c) # local to main
    
    # calling the function
    func()
    
    # updating the value of global variable 'a'
    a = a+10
    
    # printing 'a' again
    print("a: ", a) #global
