## O CÓDIGO NÃO FUNCIONA AINDA POIS TEM ALGUMAS FUNÇÕES EM JS
## DO EXEMPLO QUE USEI E PRECISO DESCOBRIR AINDA COMO CONVERTER ISSO
## PARA PYTHON
## Link do exemplo: https://observablehq.com/@khxu/dynamic-programming-with-coins

def make_change(value):
    coins = [1, 5, 10, 21, 25]
    change_table = map([[0, 0]])

    for i in range(value):
        for coin in coins:
            if ((i - coin) == 0):
                ##VERIFICAR COMO FAZER ISSO EM PYTHON
                set(change_table, i, 1)
            elif i - coin > 0:
                ###VERIFICAR COMO FAZER ISSO EM PYTHON
                change_table.set(i, 1 + change_table.get(i - coin))
                # change_table.__setattr__()
                # change_table.__getattribute__()
    
    return change_table.get(value)

print(make_change(63), 'should be equal 3') ## 3 moedas de 21 centavos