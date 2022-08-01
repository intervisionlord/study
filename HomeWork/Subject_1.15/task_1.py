"""Задача 1.

Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов.
emails = "zuck26@facebook.com  
page33@google.com  
jeff42@amazon.com"  

# требуеый вывод
[('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
"""

import re

emails = 'zuck26@facebook.com \
    page33@google.com \
    jeff42@amazon.com'  
newList = []

def mailParse(emails):
    emailsList = re.split('\s', emails)
    length = len(emailsList)
    for lenLinst in range(length):
        for item in emailsList:
            if item == '':
                emailsList.pop(emailsList.index(item))
    
    for item in emailsList:
        newList.append(tuple(re.split('[@|\.]', item)))
    print(newList)

if __name__ == '__main__':
    mailParse(emails)