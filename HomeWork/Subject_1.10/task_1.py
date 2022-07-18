"""Задача 1.
Дан одномерный массив числовых значений, насчитывающий N элементов.
Вставить группу из M новых элементов, начиная с позиции K.
"""

from array import array

mainArray = array('i', [val for val in range(0, 10)])
newData = [55, 66, 77, 88, 99]

def insertToArr(mainArray: array, newData: list):
    """Добавляет в массив значения из списка после 3-го элемента.

    Args:
        mainArray (array): Основной массив.
        newData (list): Список добавляемых элементов.
    """
    for i in newData[::-1]:
        mainArray.insert(3, i)

if __name__ == '__main__':
    print('Исходный массив:', mainArray.tolist())
    insertToArr(mainArray, newData)
    print('Новый массив:', mainArray.tolist())