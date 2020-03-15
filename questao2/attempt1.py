# coding=utf-8
import time

def calcule_amount_possibility(coins_value_list, change):
    min_coins = change
    if change in coins_value_list:
        return 1
    else:
        for i in [c for c in coins_value_list if c <= change]:
            num_coins = 1 + calcule_amount_possibility(coins_value_list, change-i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

start = time.time()
print(calcule_amount_possibility([1,5,10,55], 61))
total_time = time.time() - start
print("Tempo total de execucao %.1f seg" % (total_time))

# if __name__ == "__main__":
#     coins = [1, 5, 10, 21, 25]
#     greedy_coin_change(coins)