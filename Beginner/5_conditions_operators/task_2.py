son = int(input('son kiriting: '))
fiz = "Fiz"
biz = 'Biz'

if son%3==0 and son%5==0:
    print(fiz+biz)
elif son%3==0:
    print(fiz)
elif son%5==0:
    print(biz)
else:
    print(son)