import re

texto = "7" 

padrao = r"\d" # qualquer numero de 0 a 9

if re.fullmatch(padrao, texto): # fullmatch = tem que ser exatamente isso
    print("É um número") 
else:
    print("Não é número")



texto = "a"

padrao = r"\D" # qualquer caractere que nao seja numero 

if re.fullmatch(padrao, texto): # fullmatch = tem que ser exatamente isso
    print("Não é número")
else:
    print("É número")

#"a" → válido
#"9" → inválido
# "#" → válido



texto = "12345"

padrao = r"\d+" # somente numero, acrescentando o sinal de + e um numero ou mais 

if re.fullmatch(padrao, texto): # fullmatch = tem que ser exatamente isso
    print("Só números (vários)")
else:
    print("Inválido")


#\d = número

#+ = um ou mais
# 👉 vários números



texto = ""

padrao = r"\d*" #somente numero mais acrecentando o sinal *  pode ter nada ou pode ter mais

if re.fullmatch(padrao, texto): # fullmatch = tem que ser exatamente isso
    print("Aceitou")
else:
    print("Não aceitou")


# * = pode ter nada ou pode ter vários



texto = "123"

padrao = r"\d{3}" # quatidade de numeros exatamente 3 vezes {3}

if re.fullmatch(padrao, texto):
    print("Exatamente 3 números")
else:
    print("Quantidade errada")

# {3} = exatamente 3 vezes


texto = "1234"

padrao = r"\d{2,5}" # entre 2 e 5

if re.fullmatch(padrao, texto):
    print("Entre 2 e 5 números")
else:
    print("Fora do padrão")





texto = "A"

padrao = r"\w" # letras numeros e _

if re.fullmatch(padrao, texto):
    print("Letra ou número")
else:
    print("Outro símbolo")
#\w aceita:
#letras
#números
#_ (underline)




import re

texto = "@"

padrao = r"\W" # somente simbolos

if re.fullmatch(padrao, texto):
    print("Símbolo")
else:
    print("Não é símbolo")




import re

texto = " "

padrao = r"\s" # espaços

if re.fullmatch(padrao, texto):
    print("É espaço")
else:
    print("Não é espaço")


import re

texto = "Meu email é teste123@gmail.com e o outro é abc_99@out.com"
padrao = r"\w+"

resultado = re.findall(padrao, texto)
print(resultado)
