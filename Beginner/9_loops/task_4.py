n = (input('son kiriting:  ').split(' '))

fixed = []

for i in n:
    fix_n = ''
    while not int(i) == 0:
        fix_n += str(int(i) % 10)
        i = int(i) // 10
    fixed.append(fix_n)

print(fixed)
