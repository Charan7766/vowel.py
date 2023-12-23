import random
num=random.randint(100,1000)
while True:
    a=int(input('enter any number:-'))
    if a==num:
        print('congracts you sucessfully guessed the number',num)
        break
    elif a<num:
        print('enter a greter a number')
    elif a>num:
        print('enter a lesser number')
