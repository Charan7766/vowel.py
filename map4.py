def length(a):
    if type(a) in [list,set,tuple,dict,str,complex]:
        return len(a)
    else:
        return a
out=map(length,[1,(4,5),[7,9],{1,2}])
print(list(out))