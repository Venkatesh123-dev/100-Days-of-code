#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:20:48 2020
The Captain's Room
@author: venky
"""

k = input()
rooms = list(map(int, input().split()))
a = set()
b = set()
for room in rooms:
    if room not in a:
        a.add(room)
        b.add(room)
    else:
        b.discard(room)
        
b = list(b)
print(b[0])      

#second approach
K = int(input())

room_list = list(map(int, input().split()))
room_set = set(room_list)
sum_room_list = sum(room_list)
sum_room_set = sum(room_set)
diff = sum_room_set * K - sum_room_list

print(diff // (K - 1))