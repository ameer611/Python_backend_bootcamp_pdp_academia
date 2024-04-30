def answer():
    i = 0
    while True:
        i += 1
        yield i

for i in answer():
    print(i)

