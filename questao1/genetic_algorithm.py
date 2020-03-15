# coding=utf-8
import random

def genetic_alg(individuo):
    pop_inicial = populacao_inicial()
    fitness_function(pop_inicial, individuo)
    
## fitness function é onde será avaliada a aptidão de cada indivíduo conforme a população dada 
def fitness_function(populacao, individuo):
    aptidao = 0
    for pop in populacao:
        for indv in individuo:
            if indv == pop:
                aptidao = aptidao + 1

    

# def mutacao(individuo):
    

def populacao_inicial():
    populacao_inicial = []
    for i in range(20):
        populacao_inicial.append(random.randint(0,1))
    return populacao_inicial

if __name__ == "__main__":
    individuo = [0, 1, 0, 1, 0, 1]
    print(genetic_alg(individuo))