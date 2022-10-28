''' 
    Tendo como dados de entrada a altura e o sexo
    de uma pessoa. construa um algoritmo que
    calcule seu peso ideal utilizando as seguintes
    formulas
    para homens (72.7 * altura) - 58
    para mulheres (62.1 * altura) - 44.7
'''
# .lower() serve para converter os caracteres da variavel de maiusculo para minusculo

sexo = str(input("Informe seu sexo m(masculino) ou f(feminino): "))
altura = float(input("Informe sua altura"))

if sexo.lower() == 'm':
    peso_ideal = (altura * 72.7) - 58

elif sexo.lower()== 'f':
     peso_ideal = (altura * 62.1) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido")

#saida
print("Seu peso ideal é {0:.2f}".format(peso_ideal))
   