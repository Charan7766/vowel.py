def add_int(arr):
    out=0
    for i in arr:
        if type(i)==int:
            out+=i
    print(out)
add_int([1,2,3,'and',[1,2,3]])
add_int([5,9,'s'])
