# coding=utf-8
import random, string

## REFERÊNCIA: https://www.electricmonk.nl/log/2011/09/28/evolutionary-algorithm-evolving-hello-world/  
    
## fitness function é onde será avaliada a aptidão de cada indivíduo conforme a população dada
def calc_fitness(source, target):
    aptidao = 0

    for sc, tg in zip(source, target):
        if sc == tg:
            aptidao = aptidao+1
    return aptidao

## a mutação é onde são gerados novos indivíduos para uma nova avaliação de população ideal
def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]

    # Aqui é onde é feito o crossover (mistura de DNAs)
    # escolhe randomicamente os indivíduos para fazer o crossover
    start = random.randint(0, len(parent2['dna']) - 1)
    stop = random.randint(0, len(parent2['dna']) - 1)
    if start > stop:
        stop, start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]

    # Mutate one position
    charpos = random.randint(0, len(child_dna) - 1)
    child_dna[charpos] = child_dna[charpos] + random.randint(-1,1)
    child_fitness = calc_fitness(child_dna, target)
    return({'dna': child_dna, 'fitness': child_fitness})

## Gera parentes randômicos
def random_parent(genepool):
    wRndNr = random.random() * random.random() * (GENSIZE - 1)
    return(genepool[wRndNr])

def populacao_inicial():
    populacao_inicial = []
    for i in range(20):
        populacao_inicial.append(random.randint(0,1))
    return populacao_inicial

if __name__ == "__main__":
    target = [1, 0, 1, 0, 1, 0]
    source = populacao_inicial()

    GENSIZE = source
    genepool = []
    number =0
    for i in range(0, GENSIZE):
        # dna = [j for j in range(0, len(target))]
        for j in range(0, len(target)):
            dna = j
        fitness = calc_fitness(dna, target)
        candidate = {'dna': dna, 'fitness': fitness }
        genepool.append(candidate)
    
    child = None

    while True:
        genepool.sort(key=lambda candidate: candidate['fitness'])

        if genepool[0]['fitness'] == 0:
            # Target reached
            break

        parent1 = random_parent(genepool)
        parent2 = random_parent(genepool)

        child = mutate(parent1, parent2)
        if child['fitness'] < genepool[-1]['fitness']:
            genepool[-1] = child
        print(child)
    print(child)