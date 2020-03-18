# coding=utf-8
import random, string
    
## fitness function é onde será avaliada a aptidão de cada indivíduo conforme a população dada
def calc_fitness(source, target):
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
def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]

    # Mix both DNAs
    start = random.randint(0, len(parent2['dna']) - 1)
    stop = random.randint(0, len(parent2['dna']) - 1)
    if start > stop:
        stop, start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]

    # Mutate one position
    charpos = random.randint(0, len(child_dna) - 1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1,1))
    child_fitness = calc_fitness(child_dna, target)
    return({'dna': child_dna, 'fitness': child_fitness})

def random_parent(genepool):
    wRndNr = random.random() * random.random() * (GENSIZE - 1)
    wRndNr = int(wRndNr)
    return(genepool[wRndNr])


if __name__ == "__main__":
    target = "Hello, World!"

    GENSIZE = 20
    genepool = []
    for i in range(0, GENSIZE):
        dna = [random.choice(string.printable[:-5]) for j in range(0, len(target))]
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
