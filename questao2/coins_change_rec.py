# coding=utf-8
import sys

#Meu algoritmo apresentado na última aula demorava MUITO porque era 
#um algoritmo RECURSIVO de FORÇA BRUTA e NÃO GULOSO.
#Todas as possibilidades eram testadas.

## Coin Change resolvido com recursão e abordagem gulosa 
# A abordagem gulosa não funciona em todas as combinações de valores e moedas.

#Exemplo que funciona
# Troco desejado: R$50 centavos
# Moedas disponiveis: (30, 20, 10, 1)
# No exemplo acima é possível gerar o valor 50 tentando usar as moedas de maior valor.
# 30 + 20, sendo esta a resposta correta.
# 
# Exemplo que NÃO funciona
# Troco desejado R$63 centavos
#[1, 5, 25, 21, 10] => [25, 21, 10, 5, 1]
# O algoritmo vai tentar manter as moedas de maior valor, gerando o resultado:
# 25 + 25 + 10 + 1 + 1 + 1 => 6 moedas
#Esse não é o resultado correto.
#Deveria ser 21 + 21 + 21 => 3 moedas
## Complexidade de Tempo: 
# pior caso: O(nˆm)
# melhor caso: Ω(1)
# médio caso: Θ((nˆm)/2)

def coinchange_recursivo_guloso(moedas, troco):
    moedas.sort(reverse=True) #Ordeno de forma decrescente (abordagem GULOSA)
    return _coinchange(moedas, troco)
    
def _coinchange(moedas, troco):
    ## caso base: Conseguiu ua combinação de Moedas que represenye o troco
    if (troco == 0): 
        return 0
    
    resultado = -1 #Caso não consiga encontrar combinação que funcione, retorno -1

    # percorre cada moeda e verifica se a moeda atual é menor ou igual ao troco
    for i in range(0, len(moedas)):
        if (moedas[i] <= troco):
            resultado = _coinchange(moedas, troco - moedas[i]) 

            #Caso não tenha sido encontrado moeda menor que o troco
            #Ex: Não existe moeda de valor "1" e o troco necessário é 1
            #o retorno da chamada recursiva é "-1" (impossível gerar troco) e isso é passado adiante.
            if resultado == -1:
                return resultado
            
            ##Retorno padrão que contabiliza a quantidade de moedas usadas até então
            return resultado + 1

    return resultado 

if __name__ == "__main__":
    moedas = [1, 5, 25, 21, 10]
    troco = 63
    qtde_min_moedas = coinchange_recursivo_guloso(moedas, troco)
    print("A quantidade minima de moedas eh {}".format(qtde_min_moedas))