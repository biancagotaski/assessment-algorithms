# coding=utf-8
import time

'''
Solução recursiva e gulosa
## algoritmo guloso quer dizer que só se preocupa em resolver
# problemas locais, logo, pode não gerar a melhor solução
# por não olhar para o contexto global dado o problema
'''

coins = [1, 5, 10, 21, 25]

possibilities = []

def make_change(amount):
    if amount == 0:
        return 0
    else:
        min_found = float('inf')
    
    for coin in coins:
        if ((amount - coin) >= 0):
            min_for_this_path = make_change(amount - coin) + 1

            if min_for_this_path < min_found:
                min_found = min_for_this_path
        # possibilities.append([coin])
    return min_found

start = time.time()
result = make_change(63)
total_time = time.time() - start
print("Tempo total de execucao %.1f seg(s)" % (total_time))
print("Quantidade minima de moedas usadas para a troca", result)
# print("Moedas que podem ser usadas para o troco: ", possibilities)