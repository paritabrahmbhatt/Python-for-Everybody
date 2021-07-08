# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:17:09 2021

@author: GEC DAHOD
"""
#Create an array with 5 values & delete the value at index no. 2
#without using in-built function. 
from array import *
arr = array('i',[1,12,13,1,321,33,21,14])
c = 0
for i in arr:
    if(c == 2):
        arr.pop(x)
        break
print(arr)