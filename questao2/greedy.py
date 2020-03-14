def greedy_coin_change(coins):
    n = len(coins)
    amount_change = 63
    count = 0
    aux = 0
    
def calcule_amount_coins(value):
    for i in range(n):
        last_el = n-1 ## get the last array element
        aux = i+1
        if last_el == amount_change:
            print("O troco é de", last_el, "centavos. Entregue com", count, "moedas")
            return amount_change
        elif last_el < amount_change:
            change += last_el
            calcule_amount_coins(change)
        elif last_el > amount_change:
            last_el = last_el - 1
            calcule_amount_coins(coins[last_el])

if __name__ == "__main__":
    coins = [1, 5, 10, 21, 25]
    greedy_coin_change(coins)    
    