# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:11:56 2021

@author: GEC DAHOD
"""
# Print Pattern
# 
# #  
# # #  

n = 5
i = 0
while i < n:
    j = 0
    while j <= i:
        print("#", end = " ")
        j += 1
    i += 1
    print("\n")
    