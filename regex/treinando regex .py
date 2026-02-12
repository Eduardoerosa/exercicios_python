import re

texto = "Eu estudo Python todos os dias"
padrao = "Python"

resultado = re.search(padrao, texto)

print(resultado)
