# Faça um algoritimo para calcular o estoque medio de uma peça

#entradas
quantidade_minima = int(input("Informe a quantidade minima: "))
quantidade_maxima = int(input("Informe a quantidade maxima: "))

#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2

#saida
print("O estoque médio é: {0}".format(estoque_medio))