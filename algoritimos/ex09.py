'''
    elabore um algoritmo que leia um numero
    se positivo armazene-o em 'a'
    se for negativo em 'b'
    no final mostre o resultado
'''

numero = int(input("Informe um numero: "))
if numero > 0:
    a = numero
    print("seu numero é positivo")
else:
    b = numero
    print("seu numero é negativo")
