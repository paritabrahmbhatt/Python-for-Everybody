# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:56:16 2021

@author: GEC DAHOD
"""
#Python Program for compound interest

p = int(input("Enter Principle value: "))
n = int(input("Enter the period: "))
r = float(input("Enter the rate: "))

x = (1 + (r/100))**n
a = p * x
i = a - p
print("Compound interest is ",i)