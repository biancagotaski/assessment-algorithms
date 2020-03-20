# coding=utf-8
import time
import sys

## dynamic programming solution
## time complexity: 
# pior caso: O(nˆm)
# melhor caso: Ω(1) - se receber um vetor que só possui uma moeda disponível e o troco é exatamente o valor dessa moeda
# médio caso: Θ((nˆm)/2)
def min_coin_change(coins, coins_vet_size, change):
    # a variável result vai guardar sempre os valores mínimos até que a menor moeda seja encontrada
    # result[i] will be storing the minimum  
    # número de moedas para cada valor de i
    # number of coins required for i value.
    # Então a result[change] terá o resultado  
    # So result[change] will have result 
    result = [0 for i in range(change + 1)] 
  
    # Base case (If given value change is 0) 
    # Caso base (se o valor da troca é zero)
    result[0] = 0
  
    # Initialize all result values as Infinite 
    # Inicializo todos os valores dessa result como infinito, uma vez que eu ainda não conheço os valores
    for i in range(1, change + 1): 
        result[i] = sys.maxsize 
  
    # Calcula o mínimo de moedas para todos os valores a partir de 1 para o troco
    # Compute minimum coins required  
    # for all values from 1 to change 
    for i in range(1, change + 1): 

        # percorre todas as moedas menores do que o valor de i      
        # Go through all coins smaller than i
        ## ESSE i TÁ ME DEIXANDO CONFUSA
        for j in range(coins_vet_size):
            if (coins[j] <= i):
                sub_res = result[i - coins[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < result[i]): 
                    result[i] = sub_res + 1
    return result[change] 

if __name__ == "__main__":
    coins = [1, 5, 25, 21, 10]
    vet_size = len(coins)
    change = 63 ## troco estabelecido pelo assessment
    start = time.time()
    minimun_coin_to_change = min_coin_change(coins, vet_size, change)
    end = time.time() - start
    print(end)
    print("A quantidade minima de moedas eh: " ,minimun_coin_to_change)