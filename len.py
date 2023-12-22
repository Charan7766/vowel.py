num=int(input('enter any number'))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print('given number is prime')
else:
    ("it is not a prime number")
