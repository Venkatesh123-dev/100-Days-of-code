#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:19:04 2020

@author: venky
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader.
"""
#approach 1
def get_ans(n, arr):
    max_n = arr[-1]
    ans = []
    for i in range(1,n+1):
        if arr[-i] >= max_n:
            max_n = arr[-i]
            ans.append(arr[-i])
    print(*ans[::-1], sep = ' ')
   


get_ans(6, [1, 22, 45, 19, 5, 6])


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        arr = list(map(int, input().split()))
        get_ans(6, arr = [1, 2, 3, 4, 5, 6])  

"""
leaders an array :

    i/p: [7,10,4,15,11,2,14]
    o/p: 15, 14

    i/p: [10,20,30] #ascending order  small to big 
    o/p : 30


    i/p:[30,20,10] #desc order   big to small
    o/p :30,20,10
    
"""    

#naive approach

def leaders1(arr,n):
    for i in range(n):
        flag = 0
        for j in range(i+1,n):
            if arr[j]>=arr[i]:
                flag = 1
                break
        if flag==0:
            print(str(arr[i])+" ")


arr = [7,10,4,10,6,5,2]
leaders1(arr,len(arr))


def leaders(arr,n):
    s = ""
    curr_leader = arr[n-1]
    s = str(curr_leader)+" "+s
    for i in range(n-2,0,-1):
        if curr_leader<arr[i]:
            curr_leader = arr[i]
            s = str(curr_leader)+" "+s

    print(s)

            
arr = [7,10,4,10,6,5,2]
leaders(arr,len(arr))
