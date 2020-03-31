# coding=utf-8
import random

def populacao_inicial():
    populacao_inicial = []
    for i in range(20):
        populacao_inicial.append(random.randint(0,1))
    return populacao_inicial

def calc_aptidao(pop_desejada, pop_atual):
    aptidao = 0
    for sc, tg in zip(pop_desejada, pop_atual):
        if(sc == tg):
            aptidao = aptidao +1
    return aptidao

## a mutação é onde são gerados novos indivíduos para uma nova avaliação de população ideal
def mutacao(parente):
    individuo_escolhido = random.randrange(0, len(parente))
    return individuo_escolhido

## crossover é onde ocorre a troca de indivíduos. Onde o mais apto sobrevive e menos apto sai da lista.
def crossover(individuo_escolhido, individuos):
    ## escolhe dois individuos aleatórios da população original para realizar o crossover
    ## e que os individuos não são repetidos
    indv1, indv2 = random.sample(pop_inicial, 2)
    if indv1 == individuos[individuo_escolhido]:
        individuos[individuo_escolhido] = indv2
    else:
        indv1
    return individuos

## os parentes são gerados após a mutação
def parentes_gerados(pop_inicial, pop_desejada, tam_pop):
    genes = []
    while len(genes) < pop_desejada:
        _min = min(pop_desejada-len(genes),len(pop_inicial))
        if min(pop_desejada-len(genes),len(pop_inicial)) < tam_pop:
            genes.extend(random.sample(pop_inicial,_min))
    return genes

def exibir_resultado(pop_atual):
    populacao_gerada = list(pop_atual)
    populacao_gerada = [ int(p) for p in populacao_gerada]
    aptos = calc_aptidao(pop_desejada, pop_atual)
    print('{}\t{}\t{}\t{}'.format("aptos:", aptos, "população gerada:", populacao_gerada))

if __name__ == '__main__':

    pop_inicial = populacao_inicial()
    pop_desejada = [1,0,1,0,1,0]
    tam_max_pop = 30

    random.seed()
    parente = parentes_gerados(pop_inicial, len(pop_desejada), tam_max_pop)
    individuo_mais_apto = calc_aptidao(pop_desejada, parente)
    qtde_geracoes = 0

    individuos = list(parente)

    while True:
        individuo_escolhido = mutacao(parente)
        populacao_gerada = crossover(individuo_escolhido, individuos)
        indv_apto = calc_aptidao(pop_desejada, populacao_gerada)
        ## ordena os indivíduos aptos
        ## complexidade do sort do python é de O(n log n) no pior caso
        ## ele usa o algoritmo de ordenação Timsort que usa merge sort como base
        sorted(populacao_gerada)
        qtde_geracoes += 1
        exibir_resultado(populacao_gerada)
        if indv_apto >= len(parente) or qtde_geracoes == 1000:
            print("Quantidade de geracoes:", qtde_geracoes)
            print("Individuo mais apto:", indv_apto)
            break
        individuo_mais_apto = indv_apto
        parente = populacao_gerada