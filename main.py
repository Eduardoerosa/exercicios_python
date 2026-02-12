import os

usuarios = {
}


def menu_opcoes():
    
    print (
    "1 para cadastrar usuarios \n"
    "2 par listar \n"  
    "3 para alternar \n" 
    "4 para verificar \n" 
    "e outros numeros para voltar para o menu"
    "")


def voltar_ao_menu():
    digite_qualquercoisa = input("diigte qual coisa :")
    limpar_tela()
    main()

def menu():
    menu_opcoes()
    menu = int(input("digite uma das opçoes:"))
    if menu == 1:
        print ("cadastrando usuario :")
        cadastrar_usuarios()
    elif menu == 2:
        print ("listando usuario :")
        listar_usuarios()
    elif menu == 3:
        print ("alternar usuarios")
        alternar_usuarios()
    elif menu == 4:
        print ('verificar os acessos')
        verificar_acesso()
    else:
        print ("voltando ao menu")







def limpar_tela():
    os.system('cls')


def cadastrar_usuarios():
    nome = input("digite o nome do usuario: ")
    idade = int(input("digite a idade: "))
    ativo = True
    usuarios['nome'] = nome
    usuarios['idade'] = idade
    usuarios['ativo'] = ativo
    voltar_ao_menu()
    




def listar_usuarios():
    for usuario in usuarios.values():
        print(usuario['nome'],usuario['idade'],usuario['ativo'])
    voltar_ao_menu()
   



def alternar_usuarios():
    nome_alterar = input("digite o nome para alterar :")
    for usuario in usuarios.values():
        if usuario['nome'] == nome_alterar:
            if usuario['ativo']:
                usuario['ativo'] = False
            else: 
                usuario['ativo'] = True
    else:
        print  ("usuario nao encontrado")
    voltar_ao_menu()



def verificar_acesso():
    nome_verificar = input("diigte o nome que quer verificar")
    for i in usuarios:
        nome_usuario = i['nome']
        if nome_usuario == nome_verificar:
            if usuarios['ativo'] and usuarios['idade'] >= 18:
                print ('acesso liberado')
            else:
                print ('acesso bloqueado')
    voltar_ao_menu()

    


def main():
    menu()
    





if __name__ == "__main__":
    main()