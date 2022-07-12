"""Задание 2:

Напишите функцию search_substr(subst, st), которая принимает 2
строки и определяет, имеется ли подстрока subst в строке st. В случае
нахождения подстроки, возвращается фраза «Есть контакт!», а иначе
«Мимо!». Должно быть найдено совпадение независимо от регистра
обеих строк.
"""

def search_substr(subst: str, st: str):
    """Поиск подстроки в строке

    Args:
        subst (str): искомая подстрока
        st (str): строка
    """
    if len(subst) <= len(st):
        if subst.lower() not in st.lower():
            sOut = 'Мимо!'
        else:
            sOut = 'Есть контакт!'
    else:
        sOut = 'Подстрока не может быть больше строки'
    return sOut
    
st = input('Введите строку: ')
subst = input('Введите подстроку: ')

print(search_substr(subst, st))