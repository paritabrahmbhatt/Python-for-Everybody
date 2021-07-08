# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:01:03 2021

@author: GEC DAHOD
"""


# Python Program to check Armstrong Number

a = int(input("Enter: "))
b = a
c = a
d = 0
r = 0; ans = 0
while(a>0):
    a //= 10
    d += 1
#print(d)
for i in range(1,d+1):
    r = b % 10
    b //= 10
    ans = ans + pow(r,d)
if(c == ans):
    print("It's an amstrong number")
else:
    print("Not an amstrong number")
    
