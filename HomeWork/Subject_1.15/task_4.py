"""Задача 4.
Очистите следующий твит, чтобы он содержал только одно сообщение пользователя.
То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code
today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats' 

требуеый вывод
'Good advice What I would do differently if I was learning to code today'
"""

import re

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
regex = re.compile('(\sRT\s)|(cc:\s)|(@[\w:]+)|(#[\w]+)|(http[\w\W]+)')
print(re.sub(regex, '', tweet))