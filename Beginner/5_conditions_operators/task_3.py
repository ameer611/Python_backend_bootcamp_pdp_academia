a = int(input("a sonini kiriting:  "))
b = int(input("b sonini kiriting:  "))
c = int(input("c sonini kiriting:  "))

diskriminant = b**2-4*a*c
yechim = 0
if diskriminant>0:
    yechim=2
elif diskriminant<0:
    yechim=yechim
else:
    yechim=1

print(f"Kvadrat tenglamaning {yechim} ta yechimi bor.")