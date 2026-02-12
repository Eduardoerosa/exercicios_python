a = int(input("digite o valor"))
b = int(input("digite o valor"))
c = int(input("digite o valor"))

if a < 0 or b < 0 or c < 0:
    print("os dias nao podem ser negativos")
else:
    total = a + b + c
    print (f"o resultado e de {total}")