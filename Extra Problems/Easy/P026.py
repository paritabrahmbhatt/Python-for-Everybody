'''
Create a nested loop that produces the output below.
....1
...2
..3
.4
5
'''
i = 0
for i in range(1,6):
  for k in range(5,0,-1):
    if(i==k):
      print(i)
      break
    else:
      print('.',end='')