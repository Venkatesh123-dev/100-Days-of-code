#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:12:30 2020
program to find the addition of two numbers using 4 different ways.
@author: venky
"""

#1) Simply take input from the user and typecast to an integer at the same time after that performing addition operation on the both number.
if __name__ == "__main__" :

    # take input from user
    a = int(input())
    b = int(input())

    # addition operation perform
    sum_num = a + b
    
    print("sum of two number is: ",sum_num)

#2) Using a user-defined function for doing the sum of two numbers.
# define a function for performing 
# addition of number
def sum_num(a,b) :
    
    return a + b

# Main code
if __name__ == "__main__" :

    a = int(input())
    b = int(input())

    print("sum of two number:",sum_num(a,b))

#3) We are taking the input from user in one line after that typecast into an integer and stored them in the list then use sum() inbuilt function which returns the sum of elements of the list.
if __name__ == "__main__" :    
	# take input from the user in list
	a = list(map(int,input().split()))

	# sum function return sum of elements 
	# present in the list
	print("sum of two number is:",sum(a))

#4) We are taking the input from user in one line and store them in two different variables then typecast both into an integer at the time of addition operation.
if __name__ == "__main__" :
    
    # take input from the user in a and b variables
    a,b = input().split()

    # perform addition operation
    rslt = int(a) + int(b)
    
    print("sum of two number is:",rslt)
    