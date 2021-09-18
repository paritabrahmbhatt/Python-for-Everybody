import random
def name_to_num(name):
    if name == 'rock':
        num = 0
    elif name == 'spock':
        num = 1
    elif name == 'paper':
        num = 2
    elif name == 'lizard':
        num = 3
    else:
        num = 4
    return num

def number_to_name(num):
    if num == 0:
        return 'rock'
    elif num == 1: 
        return 'spock'
    elif num == 2:
        return 'paper'
    elif num == 3:
        return 'lizard'
    else:
        return 'scissor'
com_num = random.randrange(0,4)
name = input()
num = name_to_num(name)
print("Player chooses:", name)
print("Computer chooses:",number_to_name(com_num))

def rpsls(x,y):
    if (x==0 and y==4) or (x==4 and y==0):
        if(x<y):
            print("Player wins!!!")
        else:
            print("Computer wins!!!")
    else:
        if (x>y):
            print("Player wins!!!")
        elif(x==y):
            print("It's a tie!")
        else:
            print("Computer wins!!!")
rpsls(num,com_num)
        
