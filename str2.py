a=[2,3,4]
b=[5,6,7]
c=[8,9,1]

out=[]
for i,j,k in zip(a,b,c):
  out=out+[i]+[j]+[k]
print(out)