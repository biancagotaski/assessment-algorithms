# coding=utf-8
class Solution(object):
    def __init__(self):
        ## guardar o menor número de moedas a serem usadas no troco para cada valor de coin. Key = valor, value = menor número de moedas
        self.mem = {0:0} #Dicionário que está visível para ambas função
        # moedas_usadas = []
        
    ## é guloso por ordenar moedas de modo que pegue as de menor valor primeiro
    def coinChange(self, coins, amount):
        coins.sort()
        minCoins = self.getMinCoins(coins, amount)
        
        if minCoins == float('inf'):
            return -1
        
        return minCoins
    
    def getMinCoins(self, coins, amount):
        
        ## se o valor do troco já estiver no dicionário, poupa de buscar pelo vetor de moedas novamente
        if amount in self.mem:
            return self.mem[amount]
        
        ## enquanto ainda não tenho a quantidade mínima de moedas, elas são desconhecidas
        minCoins = float('inf')

        ## enquanto a diferença do valor do troco e a atual moeda for maior do que zero
        for c in coins:
            if amount - c <  0:
			    break
            ## executo a função para descobrir o minCoin novamente,
            ## mas dessa vez passando a diferença entre o valor do troco e a moeda atual
            numCoins = self.getMinCoins(coins, amount - c) + 1
            # self.moedas_usadas.append(numCoins)
            minCoins = min(numCoins, minCoins)
        
        self.mem[amount] = minCoins
        
        return minCoins

    # def coins_used(self):
    #     ## retorna as moedas usadas para o troco
    #     return self.moedas_usadas

        
if __name__ == "__main__":
    coins = [1, 5, 25, 21, 10]
    amount = 63
    minCoinChange = Solution()
    # moedas_usadas_troco = minCoinChange.coins_used()
    print("Quantidade minima de moedas para o troco:", minCoinChange.coinChange(coins, amount))
    # print("Moedas usadas no troco:", moedas_usadas_troco)