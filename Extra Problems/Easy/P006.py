# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:51:57 2021

@author: GEC DAHOD
"""
#Python Program for simple interest

p = int(input("Enter the amount of principle: "))
n = int(input("enter the number of years: "))
r = float(input("Enter the rate: "))

sr = (p*n*r)/100
print("Simple interest: ",sr)