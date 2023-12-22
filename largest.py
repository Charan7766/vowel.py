numbers=[1,9,11,23,65,78,143]
out=numbers[0]
out2=numbers[0]
for var in numbers:
    if out<var:
        for var in numbers:
            if out2<var and var!=out:
                out=var
print(out2)
