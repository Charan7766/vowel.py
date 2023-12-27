def sample(a):
    if 'A'<=a<='z':
        return True
    else:
        return False
out=filter(sample,'abc@15$67DEfgh')
print(list(out))  