renda_mensal = float(input("digite o valor da renda :"))
valor_da_parcela = float(input("digite o valor da parcela desejada: "))

valor = renda_mensal * 0.30
print (valor)

if renda_mensal > 2000 and valor_da_parcela <= valor:
    print ("emprestimo aprovado")
else:
    print ('emoprestimo reprovado')