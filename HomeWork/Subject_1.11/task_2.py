"""Задача 2.

Начальник отдела кадров хочет узнать, сколько мужчин-однофамильцев работает в организации.
Имеется список фамилий, и на основании этого списка нужно вычислить количество фамилий,
которые совпадают с другими.

Формат ввода: В первой строке указывается количество мужчин — сотрудников организации (N).
Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.
Формат вывода: Количество однофамильцев в организации.
"""

import collections

def populateMales():
    """Запрашивает на ввод кол-во мужчин в организации,
    а также, запрашивает фамилии.
    """
    malesCount = int(input('Введите кол-во мужчин: '))
    malesSurnames = []
    for i in range(malesCount):
        surname = str(input(f'Введите фамилию №{i+1}: '))
        malesSurnames.append(surname)
    countMutSurnames(malesSurnames)
    
def countMutSurnames(malesSurnames: list):
    """Считает количество однофамильцев в организации.

    Args:
        malesSurnames (list): список фамилий
    """
    allMalesCount = dict(collections.Counter(malesSurnames))
    mutuals = allMalesCount.copy()
    for key in allMalesCount.keys():
        if int(allMalesCount[key]) == 1:
            del mutuals[key]
    print('Количество однофамильцев: ', sum(mutuals.values()))

if __name__ == '__main__':
    populateMales()