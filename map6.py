def data_filter(a):
    if a%2!=0:
        return True
    else:
        return False
def squre(b):
    b**2
a=map(squre,filter,(data_filter,range(1,100)))
print(list(a))