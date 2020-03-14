# coding=utf-8
import random

def genetic_alg(individuo):
    pop_inicial = populacao_inicial()
    fitness_function(pop_inicial, individuo)
    
## fitness function é onde será avaliada a aptidão de cada indivíduo conforme a população dada 
def fitness_function(populacao, individuo):
    aptidao = 0
    nova_populacao = []
    for indv in individuo:
        for pop in populacao:
            if indv == pop:
                aptidao = aptidao + 1
                nova_populacao.append(aptidao)
            else:
                nova_populacao.append(aptidao)
                

    

# def mutacao(individuo):
    

def populacao_inicial():
    populacao_inicial = []
    for i in range(20):
        populacao_inicial.append(random.randint(0,1))
    return populacao_inicial

if __name__ == "__main__":
    individuo = [0, 1, 0, 1, 0, 1]
    print(genetic_alg(individuo))