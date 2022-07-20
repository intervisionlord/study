"""Задача 2.

Документ «article.txt» содержит следующий текст:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела 

Требуется реализовать функцию longest_words(file),
которая выводит слово, имеющее максимальную длину
(или список слов, если таковых несколько).
"""

import re
import collections

def longest_words(file):
    """Выводит наибольшее слово в тексте

    Args:
        file: файл с текстом
    """
    with open(file, 'r', encoding = 'utf-8') as textFile:
        article = textFile.readlines()
    newArticle = []
    for i in range(len(article)):
        article[i] = re.sub('\n', '', article[i])
        if str(article[i]).find(' ') == -1:
            newArticle.append(article[i])
        else:
            newArticle.extend(article[i].split(' '))
    articleDict = dict.fromkeys(newArticle, None)
    for key in articleDict:
        articleDict[key] = len(str(key))
    
    print(collections.Counter(articleDict).most_common(1)[0][0])

if __name__ == '__main__':
    longest_words('article.txt')