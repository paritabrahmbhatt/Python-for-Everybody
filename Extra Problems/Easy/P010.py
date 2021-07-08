# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:20:51 2021

@author: GEC DAHOD
"""
#Python program to check whether a number is Prime or not

a = int(input("Enter: "))
def primeornot(a):
    for i in range(2,a):
        if(i % 2 == 0):
            print(a, " is not a prime number")
            break
    else:
        print(a, " is a prime number")
if(a>0):
    primeornot(a)
else:
    print("Wrong input")
    
