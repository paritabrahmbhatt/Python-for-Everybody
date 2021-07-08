# -*- coding: utf-8 -*-
# Array Value form users

from array import *
arr = array('i',[])

n = int(input("Enter:"))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)
