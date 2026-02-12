
while True:
    usuario = input("digite o nome de usuario : ")
    senha = input("digite a sua senha :" )
    if len(usuario) < 5:
        print (f"o usuario tem que ter pelo menos 5 caracteres")
        continue
    elif len(senha) < 8:
        print (f"a senha tem que ter pelo menos 8 caracteres ")
        continue
    else:
        print (f'cadastro realizado com sucesso')
        break
    