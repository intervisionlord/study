"""Задача 1.

Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
то есть соединение, строк. В остальных случаях введенные числа суммируются.
"""

var1 = input('Введите первое значение: ')
var2 = input('Введите второе значение: ')

try:
    print(float(var1) + float(var2))
except ValueError:
    print(var1, var2, sep = '')