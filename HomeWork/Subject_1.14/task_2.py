"""Задача 2.

Нам нужно создать программу, которая позволяет создавать
свои собственные PIN-коды для банковских карточек.
Каждый PIN-код состоит из цифр. Дополните программу, чтобы в случае,
когда пользователь вводит буквы, программа останавливалась и выводила
"Please enter a number", а когда пользователь вводит только цифры,
программа выводила PIN code is created".
"""

def pinCreate():
    getPin = input("Задайте PIN-код: ")
    result = 'PIN code is created'
    try:
        int(getPin)
    except ValueError:
        result = 'Please enter a number'
    finally:
        print(result)


if __name__ == '__main__':
    pinCreate()