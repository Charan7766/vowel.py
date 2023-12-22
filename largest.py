numbers=[1,9,11,23,65,78,43]
maxnumbers=[i for i in numbers if i==max(numbers)]
print(*maxnumbers,sep=',')