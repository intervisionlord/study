"""
Задание 1. Даны два целых числа A и В.

Выведите все числа от A до B включительно,
в порядке возрастания, если A < B, или в порядке убывания в
противном случае.
"""

firstInt = int(input('Введите первое число '))
secondInt = int(input('Введите второе число '))

def orderAsc(minRange, maxRange):
    for values in range(minRange, maxRange + 1):
        print(values, end = ' ')

def orderDesc(minRange, maxRange):
    for values in range(minRange, maxRange + 1):
        print((maxRange + 1) - values, end = ' ')

if firstInt < secondInt:
    orderAsc(firstInt, secondInt)
elif firstInt > secondInt:
    orderDesc(secondInt, firstInt)
else:
    print('Некорректный диапазон')