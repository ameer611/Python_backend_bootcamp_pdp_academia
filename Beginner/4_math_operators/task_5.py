import math

a = int(input("sonni kiriting: "))

sign = math.floor(math.log10(abs(a)))
result = a / 10 ** sign

print(f"{a} ning ilmiy ko'rinishi: {result} * 10 ^ {sign}")