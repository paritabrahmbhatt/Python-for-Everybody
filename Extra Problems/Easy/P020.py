# -*- coding: utf-8 -*-
#Create an array with 5 values & delete the value at index no. 2
#without using in-built function. 
from array import *
arr = array('i',[1,12,13,1,321,33,21,14])
c = 0
for i in range(len(arr)):
    if(i == 2):
        arr.pop(i)
        break
print(arr)
