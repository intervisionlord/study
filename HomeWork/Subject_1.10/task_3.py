"""Задача 3.
Реализовать проект – операций над массивами,
каждая подзадача реализуется в виде отдельной функции:
    - инициализация массива с помощью датчика случайных чисел. Размер массива определяет пользователь
    - сложение массивов поэлементно в случае равенства длины массивов
    - умножение массива на число осуществляется поэлементно
    - поиск общих значений двух массивов (длины массивов могут быть разные)
    - печать значений массива
    - упорядочивание значений массива по убыванию (без использования стандартных функций)
    - поиск min, max значение в массиве, среднего значения всех значений массива (без использования стандартных функций)
"""

from array import array
import random

class uArrays:
    """Создание массивов.
    
    Класс для параметрического создания массивов (для удобства).
    Можно создать пустой массив или со случайными значениями.
    Создает массивы любой длины по выбору.
    """
    
    def __init__(self, userLen: int = None):
        self.userArray = array('i', [])
        if userLen is None:
            pass
        else:
            self.userLen = int(userLen)
            for i in range(self.userLen):
                self.userArray.append(random.randint(0,999))
    def arr(self):
        return self.userArray

def arrInit():
    """Создание массивов для дальнейшей работы.

    Returns:
        array: Возвращает 2 массива для опытов.
    """

    print('\n\u25A1 Инициализация массивов')
    firstArray = uArrays(input('Введите размер первого массива: '))
    print(firstArray.arr().tolist())
    secondArray = uArrays(input('В задачах с одним массивом будет использован первый массив\n\nВведите размер второго массива: '))
    print(secondArray.arr().tolist())
    return firstArray, secondArray

def addArrays(firstArray: uArrays, secondArray: uArrays):
    """Сложение 2х массивов поэлементно.

    Args:
        firstArray (uArrays): Первый подопытный массив
        secondArray (uArrays): Второй подопытный массив

    Returns:
        array: Возвращает результирующий массив значений
    """

    print('\n\u25A1 Сложение массивов')
    if len(firstArray.arr()) != len(secondArray.arr()):
        return 'Массивы не равны'
    else:
        resultArray = uArrays()
        for i in range(len(firstArray.arr().tolist())):
            resultArray.arr().append(firstArray.arr()[i] + secondArray.arr()[i])
        return resultArray.arr().tolist()

def mltpArrays(firstArray: uArrays):
    """Умножает первый массив на число, заданное пользователем.

    Args:
        firstArray (uArrays): Первый массив

    Returns:
        array: Возвращает массив с результатами умножения
    """

    print('\n\u25A1 Умножение элементов массива на число')
    arrMultiplier = int(input('Введите множитель: '))
    resultArray = uArrays()
    for i in range(len(firstArray.arr().tolist())):
        resultArray.arr().append(firstArray.arr()[i] * int(arrMultiplier))
    return resultArray.arr().tolist()

if __name__ ==  '__main__':
    firstArray, secondArray = arrInit()
    print(addArrays(firstArray, secondArray))
    print(mltpArrays(firstArray))