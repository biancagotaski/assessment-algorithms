# coding=utf-8
import time, sys, datetime

## Coin Change Resolvido Recursão e Força Bruta (demora MUITO)
## Complexidade de Tempo: 
# pior caso: O(nˆm)
# melhor caso: Ω(1)
# médio caso: Θ((nˆm)/2)
def realiza_troco(moedas, moedas_vet_tam, troco):
    ## caso base para que a função não entre em loop
    if (troco == 0): 
        return 0
  
    # Inicializa o resultado (inicialmente tem o máximo de valor possível porque ainda vamos descobrir o resultado)
    resultado = sys.maxsize 
      
    # percorre cada moeda e verifica se a moeda atual é menor ou igual ao troco
    for i in range(0, moedas_vet_tam):
        if (moedas[i] <= troco): 
            # sub_res recebe o valor que é gerado pela recursão desta função.
            # que recebe como parâmetro o vetor de moedas, o tamanho do vetor e o calculo
            # que é a diferença entre o troco e a moeda corrente
            # por exemplo, na primeira vez deste loop
            # 63 - 1 = 62 => sub_res = 62
            sub_res = realiza_troco(moedas, moedas_vet_tam, troco - moedas[i]) 
  
            # Logo esse sub_res será menor do que o máximo permitido e se for menor do que o resultado final, 
            # o resultado final passará a ter o valor do sub resultado
            if (sub_res != sys.maxsize and sub_res + 1 < resultado): 
                resultado = sub_res + 1
                print("sub_res", sub_res)
  
    return resultado 

if __name__ == "__main__":
    moedas = [1, 5, 25, 21, 10]
    vet_tam = len(moedas)
    troco = 63
    start = time.time()
    qtde_min_moedas = realiza_troco(moedas, vet_tam, troco)
    end = time.time() - start
    end_execution = str(datetime.timedelta(seconds=end))
    print(end_execution)
    print("A quantidade minima de moedas eh: " , qtde_min_moedas)