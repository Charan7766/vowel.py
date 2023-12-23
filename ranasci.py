import random
out=[]
while len(out)<=6:
    out+=[chr(random.randint(65,90))]
    out+=[chr(random.randint(97,122))]
    out+=[chr(random.randint(0,9))]

print(out)
captcha=''
for i in out:
    print(captcha)
