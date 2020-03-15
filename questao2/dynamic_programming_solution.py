# coding=utf-8
import time

'''
Solução com programação dinâmica
## a técnica da programação dinâmica é guardar resultados de
# subproblemas e com isso não é necessário recomputá-los.
# Essa técnica reduz o tempo de execução e a complexidade do algoritmo
# fazendo-o se tornar de exponencial para polinomial, quando comparado
# com o somente recursivo
'''

coins = [1, 5, 10, 21, 25]

change_table = []

def make_change(value):
    if value == 0:
        return 0
    else:
        if len(change_table):
            return change_table[value]

        min_found = float('inf')

        for coin in coins:
            ## verifica se o valor dado como troco é maior ou igual a moeda que está sendo percorrida no momento
            if value - coin >= 0:
                ## guarda o resultado da próxima recursão que irá fazer
                ## a recursão é realizada com base no valor atual menos o valor da moeda atual mais 1
                min_for_this_path = make_change(value - coin) + 1

                ## verifica apenas se esse valor atual não é indefinido
                if len(change_table):
                    ## verifica se o valor da ultima recursão é menor do que o valor guardado
                    if min_for_this_path < change_table[value]:
                        ## se for verdade, agora essa mesma variável irá guardar o valor desta última recursão para realizar uma nova
                        change_table[value] = min_for_this_path
                    else :
                        ## mesmo se não for verdade, também irá guardar o valor, porque será comparado mais abaixo com o a quantidade mínima de moedas encontradas
                        change_table[value] = min_for_this_path
                if min_for_this_path < min_found:
                    ## guarda esse mínimo de percurssões na variável que indica o mínimo encontrado, para retorná-lo no final do algoritmo
                    min_found = min_for_this_path
        return min_found

start = time.time()
result = make_change(63)
total_time = time.time() - start
print("Tempo total de execucao %.1f seg(s)" % (total_time))
print("Quantidade minima de moedas usadas para a troca", result)