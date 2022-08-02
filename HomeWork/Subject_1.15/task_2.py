"""Задача 2.
Извлеките все слова, начинающиеся с ‘b’ или ‘B’ из данного текста
text = "Betty bought a bit of butter, But the butter was so bitter,
So she bought some better butter, To make the bitter butter better."

требуеый вывод
['Betty', 'bought', 'bit', 'butter', 'But', 'butter', 'bitter', 'bought', 'better', 'butter', 'bitter', 'butter', 'better'] 
"""

import re
text = 'Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.'

wordsList = re.sub(',', '', text).split()
result = []
for word in wordsList:
    if re.findall('^[Bb]', word):
        result.append(word)

print(result)