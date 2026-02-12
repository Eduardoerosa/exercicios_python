pessoa = {
    'nome' : 'eduardo',
    'idade' : 22,
    'cidade' : 'pouso alegre'
}

pessoa['idade'] = 33
pessoa['profissao'] = 'programador'


del pessoa ['cidade']


print (pessoa)



produto = {
    'nome': 'Teclado',
    'preco': 150,
    'estoque': 0
}


if produto['estoque'] > 0:
    produto['status'] = 'disponivel'
else:
    produto['status'] = 'indisponivel'


print(produto)


usuario = {
    'login': 'admin',
    'ativo': False
}


if usuario['ativo'] == True:
    mensagem = 'acesso liberado'
else:
    mensagem = 'Acesso bloqueado'

def listar_usuarios():
    '''
    Docstring para listar todos os usuarios 
    '''
    pass



# 6
# resposta: olha eu nao tenho a minima ideia, acho que usuaria um for para percorrer o dicionario e depois criaria uma varia =vel para armazenar as palavras iguais
