"""
Задание 4. Выполнить циклический сдвиг в списке целых чисел на указанное число
шагов.

Сдвиг также должен быть кольцевым, то есть элемент, вышедший за пределы
списка, должен появляться с другого его конца.
Для решения этой задачи можно воспользоваться следующими методами списка:
append() - добавляет элемент в конец списка,
insert() - вставляет элемент по указанному индексу,
pop() - извлекает элемент с конца списка или, если был передан индекс, по индексу.
"""

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