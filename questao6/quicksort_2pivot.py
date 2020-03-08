import random, sys

# limit recursion for debuging reasons
sys.setrecursionlimit(20)

class Quick(object):
    ## metodo construtor que possui o tamanho do array e seta o array recebido para uma variável
    def __init__(self, array):
        self.array = array
        size_arr = len(self.array)
        print(size_arr)

    ##
    def sort(self):
        self.quickSort(0,len(self.array)-1)
        return self.array

    ## realiza a troca entre os elementos. Guarda um dos valores atuais em uma variável auxiliar
    ## e realiza a troca de acordo com o valor guardado anteriormente pela auxiliar
    def swap(self, x, y):
        aux = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = aux

    def ordenate(self, lp, rp):
        
        ## se o pivô da esquerda for maior que o pivô da direita
        ## então eu realizo a troca (pelo método swap acima)
        if(self.array[lp] > self.array[rp]):
            self.swap(lp,rp)

        ## contadores para mudar o índice corrente em questão
        counter_lp = lp + 1
        counter_rp = rp -1
        index = lp + 1

        ## guarda os valores de cada índice (pivot esquerda e direita)
        pivot_value_l = self.array[lp]
        pivot_value_r = self.array[rp]

        ## enquanto o pivot da direita for maior ou igual ao pivot da esquerda
        while(counter_rp >= index):
            ## verifica se o índice corrente é menor do que o valor do pivot da esquerda
            if (self.array[index] < pivot_value_l):
                ## então eu realizo a troca e mudo o índice e contabilizo o pivot à esquerda 
                # para a próxima posição
                self.swap(counter_lp, index)
                counter_lp += 1
                index += 1
            ## se a condição acima não for verdadeira e
            ## o índice atual for maior do que o valor do pivot da direita
            elif (self.array[index] > pivot_value_r):
                ## realizo a troca e decremento o contador do pivot a direita
                self.swap(counter_rp, index)
                counter_rp -= 1
            ## se nenhuma das verificações acima são verdadeiras,
            ## então eu vou para o próximo índice para fazer a verificação com os pivots
            else:
                index += 1

        counter_lp -= 1
        counter_rp += 1

        self.swap(lp, counter_lp)
        self.swap(rp, counter_rp)

        ## depois de realizar a troca retorno os valores do pivot da esquerda e direita
        return counter_lp, counter_rp


    def quickSort(self, lp, rp):
        ## se o pivot do meio e da esquerda são os mesmos, a função retorna
        if (rp <= lp): return

        counter_lp, counter_rp = self.ordenate(lp, rp)

        ## realiza o quick sort recursivamente
        self.quickSort(lp, counter_lp - 1)
        self.quickSort(counter_lp + 1 , counter_rp - 1)
        self.quickSort(counter_rp + 1, rp)


a = [25,5,12,41,8,17,88, 34, 77,122,234, 21]

print('vetor de entrada', a)
print('vetor ordenado', Quick(a).sort())