def view(a):
    for i in a:
        if type(i) in[list,str,tuple,set,dict]:
            yield len(i)
        else:
            yield (i)
out=view([1,2,3,{4,5,6}])
print(list(out))