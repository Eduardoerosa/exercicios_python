from storage import carregar_dados, salvar_dados

usuarios = carregar_dados()

def cadastrar(nome, idade):
    user = {
        "nome": nome,
        "idade": idade,
        "ativo": True
    }
    usuarios.append(user)
    salvar_dados(usuarios)

def listar():
    return usuarios

def buscar(nome):
    for u in usuarios:
        if u["nome"] == nome:
            return u
    return None

def remover(nome):
    for u in usuarios:
        if u["nome"] == nome:
            usuarios.remove(u)
            salvar_dados(usuarios)
            return True
    return False

def ativar_desativar(nome):
    for u in usuarios:
        if u["nome"] == nome:
            u["ativo"] = not u["ativo"]
            salvar_dados(usuarios)
            return u
    return None
