"""Задача 1.
Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел.

Напишите программу, которая подсчитывает и выводит на экран общую сумму чисел,
хранящихся в этом файле.
"""

def countFNumbers():
    """Считает сумму чисел из файла."""
    
    with open('nums.txt', 'r') as numsfile:
        nums = list(numsfile.read().split())
        nums = [int(x) for x in nums]
    print(sum(nums))

if __name__ == '__main__':
    countFNumbers()