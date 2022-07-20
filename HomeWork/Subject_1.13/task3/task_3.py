"""Задача 3.

Напишите функцию reverse(in_file, out_file),
которая читает строки из файла in_file
и создает файл out_file, куда сохраняет
прочитанные строки в обратном порядке.
"""

from black import main


def reverse(in_file, out_file):
    """Читает первый файл,
    записывает строки в обратном порядке во второй файл.

    Args:
        in_file: Исходный файл
        out_file: Результирующий файл
    """
    with open(in_file, 'r') as inFile:
        inFileRows = inFile.readlines()
    if inFileRows[-1][-1] == '\n':
        pass
    else:
        inFileRows[-1] = ''.join((inFileRows[-1], '\n'))
    
    with open(out_file, 'w') as outFile:
        if inFileRows[0][-1] == '\n':
            inFileRows[0] = inFileRows[0].rstrip(inFileRows[0][-1])
        for rows in inFileRows[::-1]:
            outFile.write(rows)

if __name__ == '__main__':
    reverse('in_file.txt', 'out_file.txt')