"""
Задание 8. Выполнить циклический сдвиг в списке целых чисел на
указанное число шагов. Сдвиг также должен быть кольцевым, то есть
элемент, вышедший за пределы списка, должен появляться с другого его
конца.
"""

# Кажется задача дублируется и аналогична задаче 4  со слайдов 30-31

mainList = [0, 1, 2, 3, 4,
            5, 6, 7, 8, 9]

def listShift():
    shiftedList = mainList.copy()
    userStep = int(input('Введите величину сдвига: '))
    for iter in range(userStep):
        shiftedList.insert(0, shiftedList.pop())
    return userStep, shiftedList

definedSteps, shiftedList = listShift()

print('Исходный список: ', mainList)
print(f'Список со сдвигом на {definedSteps}: ', shiftedList)