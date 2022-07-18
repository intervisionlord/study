"""Задача 2.
Дан одномерный массив числовых значений, насчитывающий N элементов.
Поменять местами первую и вторую половины массива без использования
дополнительных массивов"""

from array import array

def swapParts(mainArray: array):
    """Меняет местами первую и вторую половину массива.

    Args:
        mainArray (array): исходный массив.
    """
    for i in range(int(len(mainArray) / 2)):
        mainArray.insert(0, mainArray.pop())

if __name__ == '__main__':
    mainArray = array('i', [val for val in range(0, 10)])
    print('Исходный массив:', mainArray.tolist())
    swapParts(mainArray)
    print('Новый Массив:', mainArray.tolist())