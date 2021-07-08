# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:39:39 2021

@author: GEC DAHOD
"""
#Python program to print all Prime numbers in an Interval

first = int(input("Enter: "))
second = int(input("Enter: "))



if first > 0 and second > 0 and first != second:
        for i in range(first,second+1):
            if i > 1:
                for j in range(2,i):
                    if(i != j and i % j == 0):
                        break
                else:
                    print(i)
else:
    print("Wrong input")

