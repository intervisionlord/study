"""
Задание 3. Дан список из 10 чисел, которые задаются случайном образом.

Сформировать словарь по следующему принципу: ключ (one, two, three):элемент
списка models_data = {“one”:1, “two”:2, “tree”:2, “four”:3...}
Задача подсчитать количество повторений значений. Пример значение 2 –
встречается дважды.
"""

models_list1 = [2, 5, 3, 5, 2, 5, 2, 4, 33, 13]
models_list2 = ['one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight',
                'nine', 'ten']
models_data = dict(zip(models_list2, models_list1))
print(models_data)