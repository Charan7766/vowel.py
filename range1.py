def generate():
    a=5
    while a:
        yield a
        a-=1
        for b in generate():
            print(b,end="")

