
# Python Program for factorial of a number

x = int(input("Enter a number: "))
ans = 1
while(x>0):
    ans *= x
    x -= 1
print("Factorial: ",ans)
