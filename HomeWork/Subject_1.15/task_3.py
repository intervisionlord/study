"""Задача 3.
Уберите все символы пунктуации из предложения
sentence = "A, very very; irregular_sentence"  

# требуеый вывод
A very very irregular sentence
"""

import re
sentence = 'A, very very; irregular_sentence'

print(re.sub('_', ' ',
             re.sub('[^\w\s]', '', sentence))
      )