''' 
    Faça um algoritmo que leia a variavel 'p'
    e verifique se ha excesso, se houver, gravar na variavel 'e'(excesso) e na variavel 'm' o valor
    da multa a pagar.
    caso contrario mostrar tais variaveis com o conteudo "zero" 
'''

e = 0
m = 0

p = float(input("Informe o peso dos peixes: "))

# processamento

if p > 50:
    m = (p - 50) * 4.00
    e = 'excesso'
    print("Você devera pagar R$ {0:.2f}".format(m))
else:
    m = 0
    e = 0
    print("Multas: {0}".format(m))
    print("Excesso: {0}".format(e))
