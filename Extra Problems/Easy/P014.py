# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 09:22:55 2021

@author: GEC DAHOD
"""
# Print Pattern
# # # # # 
# # # # # 
# # # # # 
# # # # # 
# # # # # 


i = 0
n = int(input("Enter: "))
while(i < n):
    j = 0
    while(j < n):
        print("#",end = " ")
        j += 1
    print("\n")
    i +=1
    