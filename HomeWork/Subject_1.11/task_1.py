"""Задача 1.

Каждый ученик в классе изучает либо английский, либо французский, либо оба этих языка. 
У классного руководителя есть списки учеников, изучающих английский и французский языки.
Помогите ему выяснить, сколько учеников в классе изучают только один язык.

Формат ввода: В первых двух строках указывается количество учеников,
изучающих английский и французский языки (M и N).
Затем идут M+N строк с фамилиями учеников в произвольном порядке.
Гарантируется, что среди учеников нет однофамильцев.

Формат вывода: Количество учеников, которые изучают только один язык.
Если таких учеников не окажется, в строке вывода нужно написать 0.
Пример
Ввод
3
2
Ванюта
Соколов
Васечкин
Ванюта
Михайлов
Вывод: 3
"""

import collections

mainList = ['3', '2', 'Ванюта', 'Соколов', 'Васечкин', 'Ванюта', 'Михайлов']

def onlyOneLang():
    namesList = mainList[2:]
    namesDict = dict(collections.Counter(namesList))
    resNamesDict = namesDict.copy()
    for name in namesDict.keys():
        if namesDict[name] > 1:
            del resNamesDict[name]
    print(collections.Counter(resNamesDict.values())[1])
    
if __name__ == '__main__':
    onlyOneLang()