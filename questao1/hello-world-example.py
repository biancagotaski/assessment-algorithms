# coding=utf-8
import random
    
## fitness function é onde será avaliada a aptidão de cada indivíduo conforme a população dada
def fitness(source, target):
    aptidao = 0

    for i in range(0, len(source)):
        ## ord() -> essa função retorna o número unicode do caracter passado como parâmetro
        ## target é o meu vetor alvo (populacao final)
        ## source é minha população inicial
        ## a diferença entre os vetores elevado a 2
        aptidao += (ord(target[i]) - ord(source[i])) ** 2
        ## isso é pra não permitir números negativos
    return aptidao

## a mutação é onde são gerados novos indivíduos para uma nova avaliação de população ideal
def mutate(source):
    ## pega aleatoriamente um item dessa nova população
    pos_item = random.randint(0, len(source) -1)
    parts = list(source)
    ## the chr() function recebe um unicode e retorna o caractere referente a esse unicode
    parts[pos_item] = chr(ord(parts[pos_item]) + random.randint(-1, 1))
    return (''.join(parts))
    
def look_for_fitness_population(source, target):
    aptidao = fitness(source, target)
    i = 0
    while True:
        i += 1
        m = mutate(source)
        aptidao_m = fitness(m, target)
        if aptidao_m < aptidao:
            aptidao = aptidao_m
            source = m
            print('Numero de geracoes:', i, 'Individuos aptos:', aptidao_m, 'Resultado:', m)
            print("----------------------\n")
        if aptidao == 0:
            break


if __name__ == "__main__":
    source = "jiKnp4bqpmAbp"
    target = "Hello, World!"
    look_for_fitness_population(source, target)
