# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 06:34:55 2021

@author: Parita
"""
#Given a string of binary numbers (0s and 1s), convert it to decimal number.

a = input().replace(" ", "")
ans = 0
s = ""
for i in a:
    s = i + s
for j in range(0,len(s)):
    ans = ans+(int(s[j])*(2**j))
print(ans)
