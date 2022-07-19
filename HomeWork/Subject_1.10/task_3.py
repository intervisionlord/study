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
    
    def __init__(self, userLen = None):
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
            resultArray.arr().append(firstArray.arr()[i] + secondArray.arr()[0])
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

def searchCommon(firstArray: uArrays, secondArray: uArrays):
    """Ищет общие значения в массивах.

    Args:
        firstArray (uArrays): Первый массив
        secondArray (uArrays): Второй массив

    Returns:
        list или string: Возвращает список общих значений
        или сообщение о том, что общие значения не найдены
    """
    print('\n\u25A1 Поиск общих элементов массива')
    commonValues = list(set(firstArray.arr().tolist()) &
                        set(secondArray.arr().tolist()))
    try:
        commonValues[0]
    except:
        commonValues = 'Общие значения отсутствуют'
    finally:
        return commonValues

def arrSort(firstArray: uArrays):
    """Сортирует массив по убыванию методом пузырьковой сортировки.

    Args:
        firstArray (uArrays): Первый массив

    Returns:
        array: Отсортированный массив.
    """
    print('\n\u25A1 Сортировака массива')
    
    arrLen = len(firstArray.arr())
    for i in range(arrLen - 1):
        for j in range(arrLen - i - 1):
            if firstArray.arr()[j] < firstArray.arr()[j + 1]:
                firstArray.arr()[j], firstArray.arr()[j + 1] = \
                firstArray.arr()[j + 1], firstArray.arr()[j]
    return firstArray.arr().tolist()

def minmaxArray(firstArray: uArrays):
    """Поиск минимума и максимума массива.

    Args:
        firstArray (uArrays): Первый массив

    Returns:
        tuple: Значения минимума и максимума.
    """
    print('\n\u25A1 Поиск минимума и максимума значений массива')
    arrMin = arrMax = firstArray.arr().tolist()[0]
    for i in firstArray.arr().tolist()[1:]:
        if i < arrMin: 
            arrMax = i 
        else: 
            if i > arrMax:
                arrMax = i
    return arrMin, arrMax

def mediumArray(firstArray: uArrays):
    """Поиск среднего значения элементов массива.

    Args:
        firstArray (uArrays): Первый массив

    Returns:
        float: Среднее значение.
    """
    print('\n\u25A1 Поиск среднего значения элементов массива')
    medium = sum(firstArray.arr()) / len(firstArray.arr())
    return float(medium)

if __name__ ==  '__main__':
    firstArray, secondArray = arrInit()
    print(addArrays(firstArray, secondArray))
    print(mltpArrays(firstArray))
    print(searchCommon(firstArray, secondArray))
    print(arrSort(firstArray))
    print(minmaxArray(firstArray))
    print(mediumArray(firstArray))