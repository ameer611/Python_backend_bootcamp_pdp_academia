ism = 'muhammad '
familiya = 'usmonov'
salom = 'Assalomu alaykum, '

result = salom+ism.title()+familiya.title()

result2 = "Assalomu alaykum, {} {}".format(ism.title(), familiya.title())

result3 = "Assalomu alaykum, {name} {lastname}".format(name=ism.title(), lastname=familiya.title())

print(result)
print(result2)
print(result3)
print(f"{salom} {ism.title()} {familiya.title()}")