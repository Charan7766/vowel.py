result=[]
for i in range(3,11):
    out=1
    for j in range(1,i+1):
        out*=j
        result=result+[out]
print(result)