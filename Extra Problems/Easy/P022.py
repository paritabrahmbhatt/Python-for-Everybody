# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:42:14 2021

@author: GEC DAHOD
"""
#Print lists in Python in 3 Different Ways

a = [1,2,3,4,5]

#Using loop

for i in a:
    print(i,end = " ")
print("\n")
    
#Without using loops
print("Without using loops")
print(*a)
print(*a,sep = ",")
print('\n')

#Using map
print(''.join(map(str,a)))
print('\n')
