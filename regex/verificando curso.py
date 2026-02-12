import re
texto = "Estou fazendo um curso de Python"
padrao = "curso"


resultado = re.search(padrao,texto)


print(resultado)

texto = "curso carro crso c3rso"
padrao = "c.rso"
padron  = re.findall(padrao, texto)
print (padron)


texto = "Casa 123 Rua 45 AP 9"
padrao = "\d"

resultado = re.findall(padrao, texto)
print(resultado)



texto = "Casa 123 Rua 45 AP 9"
padrao = "\d+"

resultado = re.findall(padrao, texto)
print(resultado)
