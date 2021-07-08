# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:06:09 2021

@author: GEC DAHOD
"""
#Find the index value of the number of array

from array import *
arr = array('i',[])

n = int(input("Enter:"))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

k = int(input("Enter the number: "))
l = 0
for i in arr:
    if(k == i):
        print("index of ",k," is ",l)
        break
    l+=1
else:
    print("No such number in the array")