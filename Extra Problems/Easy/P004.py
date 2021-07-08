# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:33:50 2021

@author: GEC DAHOD
"""

# Pattern
'''
* * * *
* * *
* *
*
'''

x = 0
while(x<=4):
    y = x
    while(y<=4):
        print("*",end = " ")
        y +=1
    x += 1
    print("\n")
