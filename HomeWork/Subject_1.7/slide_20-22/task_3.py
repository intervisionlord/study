"""Задание 3:

Требуется определить индексы первого и последнего вхождения
буквы в строке. Для этого нужно написать функцию first_last(letter, st),
включающую 2 параметра: letter – искомый символ, st – целевая строка.
В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None),
если же она есть, то кортеж будет состоять из первого и последнего
индекса этого символа.
"""

def first_last(letter: str, st: str):
    """Поиск индекса 1-го и последнего вхождения буквы в строке.

    Args:
        letter (str): буква
        st (str): строка
    """
    if len(letter) > 1:
        sOut = 'Введите только одну букву'
    else:
        if st.find(letter) == -1:
            sOut = (None, None)
        else:
            sOut = (st.find(letter), st.rfind(letter))
    return sOut


st = input('Введите строку: ')
letter = input('Введите букву: ')

print(first_last(letter, st))