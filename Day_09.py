#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:59:08 2020

@author: venky
"""
#find substring of string

def substring(str1,n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(str1[i:j])
            
            
str1 = "venky"
n = len(str1)
substring(str1,n)            



#reverse string in python
def reverse(str_r):
    str_r=str_r[::-1]
    return str_r



#reverse a senternce
def reverse_words(str_r):
    n=len(str_r)
    if(n==1):
        return str_r
    str2=str_r.split(" ")
    size=len(str2)
    rev_all=""
    for i in range(size):
        rev=reverse(str2[i])
        rev_all=rev_all+rev+" "
    d=reverse(rev_all)
    return d.strip()




str_r ="World is  full of faiths and sadness"
print(reverse_words(str_r))




#left rotate string
def leftRotatedString(name):
    size = len(name)

    temp = name + name

    for i in range(size):
        for j in range(size):
            print(temp[i + j], end="")
        print()


string="NETSET"
leftRotatedString(string)

#Rotation of  string
def checkrotation(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    size=len(str1)
    s=str1+str1#checking of substing condition "ANUANUA"
    if(str2 in s):
        print(str1,"is matching with",str2)
    else:
        print(str1, "is not matching with", str2)

checkrotation("ANU","NUA")



#subsequence
def subsequence(str1):
    if (len(str1)==0):
        return [" "]
    small = subsequence(str1[1:len(str1)])
    result = [" "]* (2* len(small))
    k=0
    for i in range(len(small)):
        result[k]=small[i]
        k=k+1
    for i in range(len(small)):
        result[k]=str1[0]+small[i]
        k=k+1
    return result

print(subsequence("net"))







