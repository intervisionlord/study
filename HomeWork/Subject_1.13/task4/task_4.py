"""Задача 4.

В многострочном текстовом файле prices.txt
каждая строка с помощью символа табуляции разделена на три колонки:
1. название товара,
2. количество товара и
3. цена за 1 шт.
Выведите общую стоимость заказа с точностью до копеек.
"""

import re

def finalPrice():
    """Считает общую стоиомсть заказа из списка продуктов и кол-ва."""
    with open('prices.txt', 'r', encoding = 'utf-8') as price:
        goodsList = price.readlines()
    
    for i in range(len(goodsList)):
        goodsList[i] = re.sub('\n', '', goodsList[i])
        goodsList[i] = re.split('[ \t]+', goodsList[i])
    
    goodsPrice = {}
    for i in range(len(goodsList)):
        goodsPrice[goodsList[i][0]] = round(float(goodsList[i][1]) * float(goodsList[i][2]), 2)

    print('Общая стоимость заказа:', sum(goodsPrice.values()))

if __name__ == '__main__':
    finalPrice()