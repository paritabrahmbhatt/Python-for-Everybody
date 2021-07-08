# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:02:57 2021

@author: GEC DAHOD
"""

# Find the digits of the number

a = 1234
d =0
while(a > 0):
    a = a // 10
    d += 1
print(d)