peso = float(input("digite o peso: "))
altura = float(input(" digite a altura: "))

imc = peso /(altura ** 2)


if imc < 18.5:
    print (f"o imc e de {imc} e seu peso esta abaixo: ")
elif  imc >= 18.5 and imc < 25:
    print (f" o imc foi de {imc} e seu peso esta normal: ")
else:
    print (f"o imc foi de {imc} e seu peso esta acima") 