usuario = [
    {'nome':'eduardo','idade':22,'ativo':True}
]

def menu():
    while True:
        print ("""1 - cadastrar
2 - listar 
3 - remover usuarios
4 - ativar e desativar usuario
5 - sair
        """)
        opcoes = input("digite as opçoes:")
        if opcoes == "1":
            print ("cadastrando usuario :")
            cadastrar_usuario()
        elif opcoes == "2":
            print ("listando usuario:")
            listar_usuario()
        elif opcoes == "3":
            print ("remover ")
            remover_user()
        elif opcoes == "4":
            print ("ativar/desativar usuarios")
            ativar_desativar()
        elif opcoes == "5":
            print ("saindo")
            exit()



def ativar_desativar():
    encontrar_nome = input("digite o nome do usuario :")
    encontrado = False
    for nomes in usuario:
        if nomes['nome'] == encontrar_nome:
            encontrado = True
            print (f"Nome encontrado {nomes['nome']} e ele esta {nomes['ativo']}")
            if nomes["ativo"] == True:
                nomes["ativo"] = False
                print (f" e o {nomes['nome']} desativado {nomes['ativo']}")
                break
            else:
                nomes["ativo"] = True
                print (f"o usuario {nomes['ativo']} foi ativado")
                break
        
    if not encontrado:
        print ("usuario nao encontrado")
            
        

def cadastrar_usuario():
    while True:
        nome = input("digite o nome do usuario : ")
        try:
            idade = int(input("digite a idade do usuario :"))
        except:
            print ("tente outro numerp")
        ativo = False
        if nome == "":
            print ("nao pode ser registrado nomes vazio : ")
            continue
        if idade < 0:
            print (" nao pode ser cadastardo uma idade negativa:")
            continue
        cadastrando = {
            'nome':nome,
            'idade': idade,
            'ativo':ativo
        }
        usuario.append(cadastrando)
        break



def listar_usuario():
    encontrar_nome = input("digite o nome que quer encontrar :")
    encontrado = False
    for nomes in usuario:
        if nomes['nome'] == encontrar_nome:
            print (nomes['nome'],nomes['idade'],nomes['ativo'])
            encontrado = True
            break
    if not encontrado:
        print ("usuario nao encotrado: ")

def remover_user():
    encontrar_nome = input("digite o nome que quer encontrar :") 
    encontrado = False

    for nomes in usuario:
        if nomes['nome'] == encontrar_nome:
            usuario.remove(nomes)
            print(f"Usuário {encontrar_nome} removido com sucesso!")]
            break
            encontrado = True
    if not encontrado:
        print("Usuário não encontrado.")



def main():
    menu()



if __name__ == "__main__":
    main()
