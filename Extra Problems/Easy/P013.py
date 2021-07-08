# -*- coding: utf-8 -*-
# Python program to illustrate
# Iterating over a list

l = ["Parita", "Aayush","Pinky","Pragnesh"]
for i in l:
    a = i
    for j in a: #Iteration over string
        print(j)
    print("\n")
    
print("###################################################################")

# Iterating over a tuple (immutable)
print("Iterating over a tuple (immutable)")
t = ("Parita", "Aayush","Pinky","Pragnesh")
for i in t:
    print(i)
    
print("###################################################################")

# Iterating over dictionary
print("Iterating over dictionary")
d = {1: "Pragensh", 2: "Pinky", 3:"Parita",4:"Aayush"}
for i in d:
    print(i," ",d[i])
