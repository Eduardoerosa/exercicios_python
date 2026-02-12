soma = 0

while True:
    numero = int(input("digite o numero :"))
    if numero == 0 :
        break
    else:
        soma += numero
print (f"o valor somado foi de {soma}")