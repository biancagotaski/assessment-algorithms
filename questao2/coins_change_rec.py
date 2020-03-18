# coding=utf-8
import time
import sys

## simple recursive solution
## time complexity: 
# pior caso: O(nˆm)
# melhor caso: Ω(1)
# médio caso: Θ((nˆm)/2)
def min_coin_change(coins, coins_vet_size, change):
    ## caso base para que a função não entre em loop
    if (change == 0): 
        return 0
  
    # Inicializa o resultado (inicialmente tem o máximo de valor possível porque ainda vamos descobrir o resultado)
    res = sys.maxsize 
      
    # Try every coin that has smaller value than change 
    # percorre cada moeda e verifica se a moeda atual é menor ou igual ao troco
    for i in range(0, coins_vet_size):
        if (coins[i] <= change): 
            # sub_res recebe o valor que é gerado pela recursão desta função.
            # que recebe como parâmetro o vetor de moedas, o tamanho do vetor e o calculo
            # que é a diferença entre o troco e a moeda corrente
            # por exemplo, na primeira vez deste loop
            # 63 - 1 = 62 => sub_res = 62
            sub_res = min_coin_change(coins, coins_vet_size, change-coins[i]) 
  
            # Check for INT_MAX to avoid overflow and see if 
            # result can minimized 
            # Logo esse sub_res será menor do que o máximo permitido e se for menor do que o resultado final, 
            # o resultado final recebe seu valor + 1
            ## PORQUE TEM Q SOMAR MAIS 1???
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1
  
    return res 

if __name__ == "__main__":
    coins = [1, 5, 25, 21, 10]
    vet_size = len(coins)
    change = 63
    start = time.time()
    minimun_coin_to_change = min_coin_change(coins, vet_size, change)
    end = time.time() - start
    print(end)
    print("A quantidade minima de moedas eh: " ,minimun_coin_to_change)