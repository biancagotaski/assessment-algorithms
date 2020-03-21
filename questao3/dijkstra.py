# coding=utf-8
import sys 

## grafo não dirigido :: quando é possível ir e voltar pela mesma aresta entre dois nós
## complexidade de pior caso: O(n^2)
# o pior caso é de O(nˆ2) se dá por dois loops, um dentro do outro, no algoritmo.
# Onde o algoritmo irá percorrer o vetor n vezes para o tamanho n do vetor de entrada.
class Grafo(): 
  
    ## método construtor que recebe o grafo e realiza um loop para as linhas e colunas
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    ## exibe resultado no terminal
    def mostra_resultado(self, dist): 
        print("Vertice, Distancia do nó inicial ao nó final")
        for node in range(self.V): 
            print(node, dist[node])
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 

    ## Função que encontra o vértice com a distância de menor valor
    ## mas que não necessariamente será o menor caminho do resultado final.
    def min_distancia(self, distancia, nova_distancia): 
  
        # inicializa a mínima distância para o próximo nó (como se fosse o infinito, em python)
        min = sys.maxint 
  
        # Search not nearest vertex not in the  
        # shortest path tree 

        # busca pelo vértice mais próximo dado os vértices passado por parâmetro
        for v in range(self.V): 
            if distancia[v] < min and nova_distancia[v] == False: 
                min = distancia[v] 
                min_indice = v 
  
        return min_indice 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a grafo represented  
    # using adjacency matrix representation 

    ## função que implementa de fato o algoritmo de Dijkstra
    ## para encontrar o menor caminho de um grafo, através do peso dos vértices
    def dijkstra(self, src): 
  
        distancia = [sys.maxint] * self.V 
        distancia[src] = 0
        nova_distancia = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration

            # verifica a menor distância de um vértice dado os nós próximo ao nó corrente
            # onde na primeira iteração u será igual a distância do nó inicial
            u = self.min_distancia(distancia, nova_distancia) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            nova_distancia[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree
            # 
            ## atualiza o valor da distância dos vértices adjacentes
            ## verifica se a distância atual é maior do que a nova distância 
            ## e se o algoritmo está seguindo pelo menor caminho 
            for v in range(self.V): 
                if self.grafo[u][v] > 0 and nova_distancia[v] == False and distancia[v] > distancia[u] + self.grafo[u][v]: 
                        distancia[v] = distancia[u] + self.grafo[u][v] 
  
        self.mostra_resultado(distancia) 
  
if __name__ == "__main__":
    g = Grafo(9) 
    g.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 

    g.dijkstra(0); 