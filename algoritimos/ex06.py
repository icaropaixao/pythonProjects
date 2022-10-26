# Faça um algoritmo que pergunte quanto voçe ganha por hora
# e o numero de horas trabalhadas no mês
# calcule e mostre o total do seu salario no referido mes

# entradas
valor_hora = float(input("informe o valor por hora trabalhada: "))
horas_trabalhadas = int(input("Informe quantas horas trabalhou no mês: "))

salario = (horas_trabalhadas * valor_hora )

#saida
print("Seu salario é: R${0}".format(salario))