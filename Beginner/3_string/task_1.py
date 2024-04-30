ism = 'muhammad'
salom = 'Assalomu alaykum, '

result = salom+ism

result2 = "Assalomu alaykum, {}".format(ism)

result3 = "Assalomu alaykum, {name}".format(name=ism)

print(result)
print(result2)
print(result3)
print(f"{salom} {ism}")

