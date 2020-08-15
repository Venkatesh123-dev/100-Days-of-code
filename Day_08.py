#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division
"""
Created on Sat Aug 15 20:12:12 2020

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
val= raw_input("Please enter a sentence:")
#write down your logic here

word = val.split()
words = list(reversed(word))
reversed = ' '.join(words)
print(reversed)


print("Hello, World!")

"""Task Arithmetic Operators

Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, . The second line contains the second integer, .

Constraints



Output Format

Print the three lines as explained above.

Sample Input 0

3
2
Sample Output 0

5
1
6
Explanation 0

"""

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print( a + b)
print( a - b)
print( a * b) 


"""Python: Division

Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  /

You do not need to perform any rounding or formatting operations."""



if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(  a // b)
print( a / b)




"""We can also iterate without a definite stopping point with while loops. You might use this if you want to receive input from the user of your program but you donot know how long it will take for them to be done with your code"""
grocery_item = ""
grocery_list = []
while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list then simply type: done")
    if grocery_item == 'done':
        continue
    else:
        print("adding the item to the list")
        grocery_list.append(grocery_item)
print("Here is our grocery list:")
print(grocery_list)
