"""
Задание 9. Даны два списка целых чисел одинаковый длины.

Например [5,4,3] и [2,1,3].
Сформировать третий список полученный путем
нахождения разницы меду списками, например [5-2, 4-1,3-3] итоговый
список [3,3,0]. Формирование третьего списка осуществляется с
использованием функции.
"""

firstList = [5, 4, 3]
secondList = [2, 1, 3]

def subtractList():
    resultList = []
    if len(firstList) == len(secondList):
        for valIndex in range(len(firstList)):
            resultList.append(int(firstList[valIndex]) - int(secondList[valIndex]))
        return resultList

print('Список 1:', firstList,
      '\nСписок 2:', secondList)
print('Результирующий список:',subtractList())