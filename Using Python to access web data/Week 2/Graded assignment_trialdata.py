from re import *

file = open(r'E:\parita\Python\regex_sum_42.txt')
r = sum(list(map(int,findall('[0-9]+',file.read()))))
print(r)

