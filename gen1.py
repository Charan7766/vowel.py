def squ(a,b):
    for i in range(a,b+1):
     yield(a**2)
     yield(a*2)
out=squ(5,15)
print(list(out))
