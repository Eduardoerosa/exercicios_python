import usuarios

def menu_principal():
    while True:
        print("""
1 - Cadastrar usuário
2 - Listar usuários
3 - Buscar usuário
4 - Remover usuário
5 - Ativar/desativar usuário
6 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            usuarios.cadastrar(nome, idade)

        elif op == "2":
            lista = usuarios.listar()
            for u in lista:
                print(u)

        elif op == "3":
            nome = input("Nome: ")
            u = usuarios.buscar(nome)
            if u:
                print(u)
            else:
                print("Não encontrado")

        elif op == "4":
            nome = input("Nome: ")
            if usuarios.remover(nome):
                print("Removido")
            else:
                print("Não encontrado")

        elif op == "5":
            nome = input("Nome: ")
            u = usuarios.ativar_desativar(nome)
            if u:
                print("Status alterado:", u)
            else:
                print("Não encontrado")

        elif op == "6":
            break
