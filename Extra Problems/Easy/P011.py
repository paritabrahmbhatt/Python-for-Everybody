#Python Program for n-th Fibonacci number

s = 0
a = 0
b = 1
n = int(input("Enter: "))
if(n == 0):
    print("Wrong input")
elif n == 1:
    print("0")
elif n == 2:
    print("1")

else: 
    for i in range(2,n):
        s = a + b
        a = b
        b = s
    print(s)
