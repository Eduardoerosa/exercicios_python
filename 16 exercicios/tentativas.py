tentativas = 3

while tentativas > 0:
    numero = int(input("digite um numero :"))
    if numero == 7:
        print ("acertou")
        break
    else:
        tentativas -= 1
        print (f"voce perdeu 1 tentativa resta {tentativas}")
if tentativas == 0:
    print ("bloqueado")