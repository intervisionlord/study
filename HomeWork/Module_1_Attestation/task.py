from random import randint

def listDefine():
    """Создает списки заданной длины.
    
    Размер списка определяется пользователем программы.
    Выполнить контроль ввода
    информации – число должно быть положительное и не более 20
    заполнение списка осуществляется на основе датчика случайных чисел, и реализация
    осуществляется в виде функции, которой в качестве аргумента указывается размер списка

    Returns:
        list, list: сгенерированные списки.
    """
    lenList1 = int(input('Введите размер первого списка: '))
    lenList2 = int(input('Введите размер второго списка: '))
    if lenList1 > 20 or lenList2 > 20 or lenList1 <= 0 or lenList2 <= 0:
        print('Размер списков не должен превышать 20 и быть больше 0')
        listDefine()
    firstNumbers = [randint(0, 99) for x in range(lenList1)]
    secondNumbers = [randint(0, 99) for x in range(lenList2)]
    print(firstNumbers, secondNumbers, sep ='\n')
    return firstNumbers, secondNumbers

def findMax(numsList1: list) -> int:
    """Находит максимальный элемент в списке.

    Args:
        numsList1 (list): Для операции используется 1й список

    Returns:
        int: Максимальное число в списке
    """
    result = numsList1.copy()
    result.sort()
    return result[-1]

def findElement(numsList1: list):
    """Осуществляет поиск элемента по индексу.

    Args:
        numsList1 (list): Операция производится с первым списком

    Returns:
        Возвращает индекс искомого элемента и сам элемент.
    """
    elemIndex = int(input('Введите индекс искомого элемента: '))
    if elemIndex > len(numsList1):
        print('Список не содержит столько элементов.')
    elif elemIndex > 19:
        print('Список не длинее 20 элементов. Укажите меньший индекс.')
        findElement(numsList1)
    else:
        return elemIndex, numsList1[elemIndex]

def findValue(numsList1: list, desValue: int) -> int:
    """Ищет индекс элемента по его значению.

    Args:
        numsList1 (list): Операция осуществляется с первым списком.
        desValue (int): Искомое значение

    Returns:
        int: Индекс искомого элемента
    """
    return numsList1.index(desValue)

def delValue(numsList1: list, desElement: int) -> list:
    """Удаляет элемент из списка.
    
    реализация удаления заданного элемента в списке осуществляется в виде функции, которой
    в качестве аргумента указывается список чисел, и искомое число. Функция возвращает
    результат – список без указанного элемента

    Args:
        numsList1 (list): Операция производится над первым списком
        desElement (int): Искомый элемент

    Returns:
        list: Список после удаления элемента
    """
    modList = numsList1.copy()
    modList.pop(modList.index(desElement))
    return modList

def sumLists(numsList1: list, numsList2: list) -> list:
    """Складывает списки, если их длина совпадает.
    реализация сложения списков чисел осуществляется в виде функции, которой в качестве
    аргумента указывается списки чисел. Функция возвращает результат – печать на экране
    сообщения «сложение невозможно, из-за несовпадения длин списков», или список, в котором
    выполнено сложение поэлементно двух заданных списков чисел
    
    Args:
        numsList1 (list): Первый список
        numsList2 (list): Второй список

    Returns:
        list: Список с результатами сложения элементов.
    """
    if len(numsList1) != len(numsList2):
        print('Сложение невозможно из-за несовпадения длин списков')
    else:
        summedList = []
        for i in range(len(numsList1)):
            summedList.append(numsList1[i] + numsList2[i])
    return summedList

def labStart():
    numsList1, numsList2 = listDefine()
    print('{}\nПоиск наибольшего числа и элемента по индексу\n'.format('-' * 20)
          + 'будет осуществляться по первому списку!\n{}'.format('-' * 20))
    print('Наибольшее число:', findMax(numsList1))
    elemIndex, findElemResult = findElement(numsList1)
    print('По индексу {} расположено число {}'.format(elemIndex, findElemResult))
    desValue = int(input('Введите искомое число: '))
    print('Число {} расположено по индексу {}'.format(desValue, findValue(numsList1, desValue)))
    desElement = int(input('Введите число, которое хотите удалить из списка: '))
    print('Число {} удалено из спика. Результат:'.format(desValue),
          delValue(numsList1, desValue), sep = '\n')
    print('Результат сложения списков:', sumLists(numsList1, numsList2), sep = '\n')

if __name__ == '__main__':
    labStart()