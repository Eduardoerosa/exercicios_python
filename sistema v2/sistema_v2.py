import json

ARQUIVO = "dados.json"

# ========================
# Persistência
# ========================

def carregar_dados():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

usuarios = carregar_dados()

# ========================
# Sistema
# ========================

def menu():
    while True:
        print("""
======== SISTEMA ========
1 - Cadastrar usuário
2 - Listar usuários
3 - Remover usuário
4 - Ativar/Desativar usuário
5 - Sair
=========================
""")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_usuario()
        elif op == "2":
            menu_listagem()
        elif op == "3":
            remover_usuario()
        elif op == "4":
            ativar_desativar()
        elif op == "5":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

# ========================
# Submenu
# ========================

def menu_listagem():
    while True:
        print("""
--- LISTAGEM ---
1 - Listar todos
2 - Buscar por nome
3 - Voltar
""")
        op = input("Escolha: ")

        if op == "1":
            listar_todos()
        elif op == "2":
            buscar_por_nome()
        elif op == "3":
            break
        else:
            print("Opção inválida.")

# ========================
# Funções
# ========================

def cadastrar_usuario():
    nome = input("Nome: ").strip()

    if nome == "":
        print("Nome não pode ser vazio.")
        return

    # bloqueio de duplicado
    for u in usuarios:
        if u["nome"].lower() == nome.lower():
            print("Usuário já existe.")
            return

    try:
        idade = int(input("Idade: "))
        if idade < 0:
            print("Idade inválida.")
            return
    except:
        print("Idade deve ser número.")
        return

    usuario = {
        "nome": nome,
        "idade": idade,
        "ativo": True
    }

    usuarios.append(usuario)
    salvar_dados(usuarios)
    print("Usuário cadastrado com sucesso.")

def listar_todos():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for u in usuarios:
        print(u["nome"], u["idade"], u["ativo"])

def buscar_por_nome():
    nome = input("Nome: ").strip().lower()
    encontrado = False

    for u in usuarios:
        if u["nome"].lower() == nome:
            print(u["nome"], u["idade"], u["ativo"])
            encontrado = True

    if not encontrado:
        print("Usuário não encontrado.")

def remover_usuario():
    nome = input("Nome para remover: ").strip().lower()

    for u in usuarios:
        if u["nome"].lower() == nome:
            conf = input("Tem certeza? (s/n): ").lower()
            if conf == "s":
                usuarios.remove(u)
                salvar_dados(usuarios)
                print("Usuário removido.")
            return

    print("Usuário não encontrado.")

def ativar_desativar():
    nome = input("Nome: ").strip().lower()

    for u in usuarios:
        if u["nome"].lower() == nome:
            u["ativo"] = not u["ativo"]
            salvar_dados(usuarios)
            print("Status alterado:", u["ativo"])
            return

    print("Usuário não encontrado.")

# ========================
# Start
# ========================

def main():
    menu()

if __name__ == "__main__":
    main()
