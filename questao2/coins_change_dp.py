# coding=utf-8
import time, sys

## dynamic programming solution
## time complexity: 
# pior caso: O(n * m) -> Onde N é o valor de entrada (Ex: 63) e M é a quantidade de moedas disponíveis (Ex: 5)
# melhor caso: Ω(1) - se receber um vetor que só possui uma moeda disponível e o troco é exatamente o valor dessa moeda
# médio caso: Θ(n * m) -> Igual ao pior caso. Isso é fixo. Preciso percorrer todo o troco e todas as moedas.
def realiza_troco(moedas, troco):

    # a variável resultado vai guardar sempre os valores mínimos até que a menor moeda sema encontrada
    # Então a resultado[troco] terá o resultadoado
    resultado = [0 for n in range(troco + 1)] # É +1 porque preciso da posição 63.
  
    # Não preciso marcar porque má iniciei o vetor com todas as posições
    # com valor zero.
    #resultado[0] = 0 
    # Deixei aqui para lembrar que ele para dar um troco de valor zero
    # eu preciso de zero moedas =)
  
    # Inicializo todos os valores desse resultado como infinito, 
    # uma vez que eu ainda não conheço os valores
    # Para cada possivel troco a partir de 1 até 63 (inclusive) eu considero que é infinito / impossivel dar o troco
    # enquanto ainda não explorei as moedas que tenho a disposição.
    # Esse "infinito" (valor muito grande) é importante para eu ir substituindo esse valor
    # pelo que tiver de menor
    for n in range(1, troco + 1): 
        resultado[n] = sys.maxsize 
  
    # Algoritmo em Si
    # Calcula o mínimo de moedas para todos os valores a partir de 1 para o troco
    # Para cada troco possível. Ex: 1, 2, 3, ... 63
    for n in range(1, troco + 1): 
        # percorre todas as moedas que tenho disponíveis
        # Para cada moeda. Ex: 1, 5, 25, 21 e 10
        for m in range(len(moedas)):
            if (moedas[m] <= n): #Se o valor da moeda atual é menor que o troco atual... posso usar ela
                #Obtenho o número de moedas necessárias até então para representar o valor  
                #do meu troco decrementando o valor da moeda atual.
                sub_res = resultado[n - moedas[m]]   
                # Caso já exista um valor que represente essa diferença (algo diferente de infinito)
                if (sub_res != sys.maxsize and 
                    #Se a quantidade de moedas necessárias somada com o uso desta nova for menor do que má estava registrado
                    sub_res + 1 < resultado[n]):
                    #Atualizo a quantidade de moedas necessárias para representar o valor.
                    resultado[n] = sub_res + 1
    #Retorno a última posição do vetor (Ex: 63) que é o mínimo de moedas necessárias para representar ele.
    #Caso não seja possível representar o número com as moedas disponíveis, estará sendo retornado "infinito" (maior número).
    return resultado[troco] 

if __name__ == "__main__":
    moedas = [1, 5, 25, 21, 10]
    troco = 63 ## troco estabelecido pelo enunciado
    start = time.time()
    qtde_min_moedas = realiza_troco(moedas, troco)
    end = time.time() - start
    print("Tempo de execucao:", end)
    print("A quantidade minima de moedas eh: " , qtde_min_moedas)