# coding=utf-8
import random, sys

# limita a quantidade de recursões para evitar o stack overflow
sys.setrecursionlimit(20)

class Quick(object):
    ## metodo construtor que possui o tamanho do array e seta esse array como atributo que pode 
    # ser acessado por qualquer método dentro dessa classe
    def __init__(self, array):
        self.array = array
        size_arr = len(self.array)
        print("Tamanho do vetor recebido:", size_arr)

    ## chama o método quickSort passando o array que será usado para a ordenação
    def sort(self):
        self.quickSort(0,len(self.array)-1)
        return self.array

    ## realiza a troca de posição entre os elementos. Guarda um dos valores atuais em uma variável 
    # auxiliar e realiza a troca de acordo com o valor guardado anteriormente pela auxiliar
    def swap(self, x, y):
        aux = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = aux

    def ordena(self, pivo_esquerda, pivo_direita):
        
        ## se o pivô da esquerda for maior que o pivô da direita
        ## então eu realizo a troca (pelo método swap acima)
        if(self.array[pivo_esquerda] > self.array[pivo_direita]):
            self.swap(pivo_esquerda,pivo_direita)

        ## contadores para mudar o índice corrente em questão
        count_pivo_esquerda = pivo_esquerda + 1
        count_pivo_direita = pivo_direita -1
        indice_atual = pivo_esquerda + 1

        ## guarda os valores de cada índice (pivot esquerda e direita)
        pivot_value_left = self.array[pivo_esquerda]
        pivot_value_right = self.array[pivo_direita]

        ## enquanto o pivot da direita for maior ou igual ao pivot da esquerda
        while(count_pivo_direita >= indice_atual):
            ## verifica se o índice corrente é menor do que o valor do pivot da esquerda
            if (self.array[indice_atual] < pivot_value_left):
                ## então eu realizo a troca do índice e contabilizo o pivot à esquerda 
                # para a próxima posição
                self.swap(count_pivo_esquerda, indice_atual)
                count_pivo_esquerda += 1
                indice_atual += 1
            ## se a condição acima não for verdadeira e
            ## o índice atual for maior do que o valor do pivot da direita
            elif (self.array[indice_atual] > pivot_value_right):
                ## realizo a troca de índices e decremento o contador do pivot a direita
                self.swap(count_pivo_direita, indice_atual)
                count_pivo_direita -= 1
            ## se nenhuma das verificações acima são verdadeiras,
            ## então eu vou para o próximo índice para fazer a verificação com os pivôs
            else:
                indice_atual += 1
        
        ## aproxima os dois pivôs a medida que o loop ocorre, para demonstrar que o vetor está ordenado
        count_pivo_esquerda -= 1
        count_pivo_direita += 1

        self.swap(pivo_esquerda, count_pivo_esquerda)
        self.swap(pivo_direita, count_pivo_direita)

        ## depois de realizar a troca deposição, retorno os valores do pivot da esquerda e da direita
        return count_pivo_esquerda, count_pivo_direita


    def quickSort(self, pivo_esquerda, pivo_direita):
        ## se o pivot do meio e da esquerda são os mesmos, a função retorna
        # significa que o vetor está ordenado
        if (pivo_direita <= pivo_esquerda): return

        count_pivo_esquerda, count_pivo_direita = self.ordena(pivo_esquerda, pivo_direita)

        ## realiza o quick sort recursivamente -- recursivo mesmo???
        ## o pivot da esquerda será o primeiro elemento do vetor
        ## e o pivot da direita será o último elemento do vetor
        self.quickSort(pivo_esquerda, count_pivo_esquerda - 1)
        self.quickSort(count_pivo_esquerda + 1 , count_pivo_direita - 1)
        self.quickSort(count_pivo_direita + 1, pivo_direita)

if __name__ == "__main__":
    ## Questão: Dado um vetor, ordene-o usando o algoritmo quick sort, 
    # utilizando 2 pivots e com 3 partições
    v = [884, 21, 0, 12, 35, 16, 112, 9, 11, 287, 40, 51]

    print('vetor de entrada', v)
    print('vetor ordenado', Quick(v).sort())
