usuario = "eduardo"
senha = '1234'
tentivas = 3


while tentivas > 0:
    user = input("digite o usuario: ")
    passoword = input("digite a senha : ")

    if user == usuario and passoword == senha:
        print ("login e senha corrertos usuarios logados")
        break
    else:
        tentivas -= 1
        print (f" tentativas restantes {tentivas}")

    if tentivas == 0:
        print ("usuario bloqueado")
