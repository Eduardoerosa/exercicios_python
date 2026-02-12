numero_i = int(input("digite o numero inicial: "))
numero_f = int(input("digite o numero final : "))

contador = numero_i
if numero_i < numero_f:
    while contador <= numero_f:
        print (contador)
        contador += 1

if numero_i > numero_f:
    while contador >= numero_f:
        print (contador)
        contador -= 1
  
