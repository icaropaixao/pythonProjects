'''
    Ler um numero e verificar se ele é par ou impar
    quando for par armazenar esse valor em 'p'
    quando impar armazena-lo em 'i'
    exebir 'p' e 'i'  no final
'''
p = 0
i = 0
numero = int(input("informe um numero: "))

if numero % 2 == 0:
    p = numero
else:
    i = numero 
print(p)
print(i)
     