# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:34:29 2021

@author: GEC DAHOD
"""
#Print all the elements of array

from array import *
x = array('i',[13,2,32,4,15])

for i in range(len(x)):
    print(x[i])
#a = x.buffer_info()
#print(a)
#for i in range(0,a[1]):
    #print(x[i])
#for i in x:
    #print(i)
    
###Copy the array

newarr = array(x.typecode, (a * a for a in x))
print(newarr)