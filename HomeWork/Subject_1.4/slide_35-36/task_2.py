"""
Задание 2. Значениями словаря могут быть и списки.

Допишите словарь с ключами BMW, ВАЗ, Tesla
и списками из 3х моделей в качестве значений.

# данный код
models_data = {..., "Tesla": ["Modes S", ...]}
print(models_data["Tesla"][0])
# требуемый вывод:
# Model S
"""

models_data = {'BMW': ['X3', 'X5', 'X7'],
               'ВАЗ': ['2101', '2107', '2131'],
               'Tesla': ['Model S', 'Model 3', 'Model Y']}
print(models_data['Tesla'][0])