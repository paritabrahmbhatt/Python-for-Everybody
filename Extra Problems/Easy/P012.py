# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 08:37:14 2021

@author: GEC DAHOD
"""

# Python Program to check if a given number is Fibonacci number?

n = int(input("Enter the number: "))
a = 0
b = 1
if( n == 0):
    print("Yes")
elif (n == 1):
    print("Yes")
else:
    for i in range(2,n+1):
        s = a + b
        a = b
        b = s
        if(s == n):
            print("Yes")
            break
    else:
        print("No")
        
