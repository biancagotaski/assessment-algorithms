# coding=utf-8
import time, sys

## dynamic programming solution
## time complexity: 
# pior caso: O(nˆm)
# melhor caso: Ω(1) - se receber um vetor que só possui uma moeda disponível e o troco é exatamente o valor dessa moeda
# médio caso: Θ((nˆm)/2)
def realiza_troco(moedas, moedas_vet_tam, troco):

    # a variável result vai guardar sempre os valores mínimos até que a menor moeda seja encontrada
    # número de moedas para cada valor de i
    # Então a result[troco] terá o resultado
    result = [0 for i in range(troco + 1)] 
  
    # Caso base (se o valor da troca é zero)
    result[0] = 0
  
    # Inicializo todos os valores dessa result como infinito, 
    # uma vez que eu ainda não conheço os valores
    for i in range(1, troco + 1): 
        result[i] = sys.maxsize 
  
    moedas_usadas = 0
    # Calcula o mínimo de moedas para todos os valores a partir de 1 para o troco
    for i in range(1, troco + 1): 
        # percorre todas as moedas menores do que o valor do troco
        for j in range(moedas_vet_tam):
            if (moedas[j] <= i):
                sub_res = result[i - moedas[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < result[i]): 
                    result[i] = sub_res + 1
                    moedas_usadas = moedas[j]
    print("Moeda(s) usada(s):", moedas_usadas)
    return result[troco] 

if __name__ == "__main__":
    moedas = [1, 5, 25, 21, 10]
    vet_tam = len(moedas)
    troco = 63 ## troco estabelecido pelo assessment
    start = time.time()
    qtde_min_moedas = realiza_troco(moedas, vet_tam, troco)
    end = time.time() - start
    print("Tempo de execucao:", end)
    print("A quantidade minima de moedas eh: " , qtde_min_moedas)