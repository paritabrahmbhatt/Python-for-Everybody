# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:48:42 2021

@author: GEC DAHOD
"""
# Python Program for factorial of a number

x = int(input("Enter a number: "))
ans = 1
while(x>0):
    ans *= x
    x -= 1
print("Factorial: ",ans)