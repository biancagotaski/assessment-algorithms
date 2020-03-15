# coding=utf-8

def return_change(to_return, coins = [.01, .05, .10, .25, 1.0, 5.0]):
    flag = None
    for c in coins:
        if c == to_return:  return c
        if c < to_return:
            flag = c
    temp_balance = round(to_return - flag, 2)
    return [flag] + [return_change(temp_balance)]
    
            
result = return_change(4.33) # Highly nested iterable
print(result)
