num=int(input('enter a any number'))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
        print('number is perfect')
else:
        print('number is not perfect')