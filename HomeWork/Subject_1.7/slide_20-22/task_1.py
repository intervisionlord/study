""" Задание 1.

Входные данные
Дана строка.

Выходные данные
• Сначала выведите третий символ этой строки.
• Во второй строке выведите предпоследний символ этой строки.
• В третьей строке выведите первые пять символов этой строки.
• В четвертой строке выведите всю строку, кроме последних двух
символов.
• В пятой строке выведите все символы с четными индексами (считая,
что индексация начинается с 0, поэтому символы выводятся начиная с
первого).
• В шестой строке выведите все символы с нечетными индексами, то
есть начиная со второго символа строки.
• В седьмой строке выведите все символы в обратном порядке.
• В восьмой строке выведите все символы строки через один в
обратном порядке, начиная с последнего.
• В девятой строке выведите длину данной строки.
"""

sampleString = 'Тестовая строка'


def evenIndex():
    newString = []
    for iter in range(0, len(sampleString)):
        if iter == 0 or iter % 2 == 0:
            newString.append(sampleString[iter])
    return ''.join(newString)

def oddIndex():
    newString = []
    for iter in range(0, len(sampleString)):
        if iter == 1 or iter % 2 != 0:
            newString.append(sampleString[iter])
    return ''.join(newString)

def revThrough():
    revString = sampleString[::-1]
    newString = []
    for iter in range (0, len(revString)):
        if iter == 0 or iter % 2 == 0:
            newString.append(revString[iter])
    return ''.join(newString)
        
print(sampleString, '\n')

print('1.', sampleString[2])
print('2.', sampleString[-2])
print('3.', sampleString[0:5])
print('4.', sampleString[:-2])
print('5.', evenIndex())
print('6.', oddIndex())
print('7.', sampleString[::-1])
print('8.', revThrough())
print('9.', len(sampleString))