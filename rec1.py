n=5
def fact(n,i=1):
    if i==n:
        return n
    return i*fact(n,i+1)
print(fact(n))