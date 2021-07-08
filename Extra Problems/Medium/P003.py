
#Python Program for Sum of squares of first n natural numbers

n = int(input("Enter: "))
sum = 0
for i in range(1,n+1,1):
    sum = sum + (i * i)
print(sum)
    
