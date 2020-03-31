# coding=utf-8
import sys 

## grafo não dirigido :: quando é possível ir e voltar pela mesma aresta entre dois nós
## complexidade de pior caso: O(n^2)
# o pior caso é de O(nˆ2) se dá por dois loops, um dentro do outro, no algoritmo.
# Onde o algoritmo irá percorrer o vetor n vezes para o tamanho n do vetor de entrada.
class Grafo(): 
  
    def __init__(self, qtd_vertices): 
        self.qtd_vertices = qtd_vertices 
        self.grafo = [
                [0 for col in range(qtd_vertices)] for lin in range(qtd_vertices)
            ] 
  
    ## Função que encontra o vértice com a distância de menor valor em relação ao vértice atual
    ## mas que não necessariamente será a menor distância do resultado final.
    def indc_vertice_menor_distancia(self, distancias, visitados): 
  
        ## inicializa a distância mínima para os vértices ainda não visitados (como se fosse o infinito, em python)
        menor_val = sys.maxsize 

        for vertice_destino in range(self.qtd_vertices): 
            if distancias[vertice_destino] < menor_val and visitados[vertice_destino] == False: 
                menor_val = distancias[vertice_destino]
                ## retorno o índice do vértice de menor valor (ou seja, mais próximo) em relação ao meu vértice atual 
                indice_menor_val = vertice_destino 
  
        return indice_menor_val 

    def dijkstra(self, vertc_inicial): 
        
        #Cria o Vetor que armazena as distâncias de cada vértice em relação ao vértice inicial
        ## e a primeira posição recebe o valor zero inicialmente, pois a distância do primeiro vértice para ele mesmo é zero.
        distancias = [sys.maxsize] * self.qtd_vertices 
        
        distancias[vertc_inicial] = 0
        ## Os vértices são inicializados como não visitados inicialmente
        visitados = [False] * self.qtd_vertices
  
        ## contando os vértices recebidos na entrada do algoritmo
        for i in range(self.qtd_vertices):

            #Vertice Atual é a linha da matriz
            vertice_atual = self.indc_vertice_menor_distancia(distancias, visitados)
  
            ## o vértice atual já fica marcado como sendo visitado
            visitados[vertice_atual] = True
            print("{}{}{}".format("Vertice ", vertice_atual, " acabou de ser visitado."))

            for vertice_destino in range(self.qtd_vertices):
                peso_aresta = self.grafo[vertice_atual][vertice_destino]
                #Se o peso_aresta for igual a ZERO significa que não existe essa aresta
                if peso_aresta == 0:
                    continue #Ignoro essa aresta
                #Se o vertice de destino (onde a aresta me leva) não foi visitado
                #e a distância do vértice de destino em relação ao inicial é maior que 
                #a distância do vértice atual somado ao peso da aresta, atualizo a nova distância do vértice de destino
                if visitados[vertice_destino] == False and distancias[vertice_atual] + peso_aresta < distancias[vertice_destino] :
                        distancias[vertice_destino] = distancias[vertice_atual] + peso_aresta
        
        self.mostra_resultado(distancias) 

    def mostra_resultado(self, dist):
        print("\nVertice | distancias do vértice inicial aos vértices encontrados no grafo")
        for vertc in range(self.qtd_vertices):
            print(vertc, dist[vertc])
  
if __name__ == "__main__":
    ## quantidade de vértices que o algoritmo irá receber
    g = Grafo(5)
    ## matriz adjacente
    g.grafo = [
        [0, 2, 0, 0, 0], 
        [2, 0, 5, 1, 0], 
        [0, 5, 0, 7, 0], 
        [0, 1, 7, 0, 3], 
        [0, 0, 0, 3, 0]
        ]; 
    ## definindo o vértice inicial
    g.dijkstra(0)