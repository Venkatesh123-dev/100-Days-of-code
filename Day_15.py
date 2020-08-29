#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:34:01 2020

@author: venky
"""
#merge_the_tools
from collections import OrderedDict


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

string="AABCAAADA"
k = 3
merge_the_tools(string, k)

#Introduction to Sets

def average(array):
    # your code goes here
    distinct_height = set(array)
    return sum(distinct_height )/len(distinct_height )



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
#Set .add()

stamps = set()
for _ in range(int(input())):
    stamps.add(input())

print(len(stamps))    

#Set .union() Operation
l = []
e = input()
eng = list(map(int, input().rstrip().split()))
f = input()
fre = list(map(int, input().rstrip().split()))
for i in eng:
    l.append(i)

for i in fre:
    l.append(i)
    
s = set(l)
print(len(s))

#second approach
_,eng_sub = raw_input(),set(map(int,raw_input().split()))
_,fre_sub = raw_input(),set(map(int,raw_input().split()))
print(len(eng_sub.union(fre_sub)))

#Set .intersection() Operation

_,eng_sub = raw_input(),set(map(int,raw_input().split()))
_,fre_sub = raw_input(),set(map(int,raw_input().split()))
print(len(eng_sub.intersection(fre_sub)))

#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
_,eng_sub = raw_input(),set(map(int,raw_input().split()))
_,fre_sub = raw_input(),set(map(int,raw_input().split()))
print(len(eng_sub.difference(fre_sub)))

#Set .symmetric_difference() Operation
_,eng_sub = raw_input(),set(map(int,raw_input().split()))
_,fre_sub = raw_input(),set(map(int,raw_input().split()))
print(len(eng_sub.symmetric_difference(fre_sub)))

#Set .discard(), .remove() & .pop()

n = input()
elements = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    operation = command[0]
    args = command[1:]

    if operation != 'pop':
        operation += '(' + ','.join(args) + ')'
        eval('elements.' + operation)
    else:
        elements.pop()
print(sum(elements))
    
#second approach

input()
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    commands = input().split()
    if len(commands) > 1:
        e = int(commands[1])
    if commands[0] =="pop":
        s.pop()
    if commands[0] =="remove":
        s.remove(e)
    if commands[0] =="discord":
        s.remove(e)
        
print(len(s))        
    
    
    
    
    
    
    
    
    
    
    
    
    