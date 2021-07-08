# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:16:00 2021

@author: GEC DAHOD
"""
#Print pattern

# # #
# #
#
i = 0
n = int(input("Enter: "))
for i in range(n,0,-1):
    j = i
    while(j > 0):
        print("#", end = " ")
        j -= 1
    print("\n")