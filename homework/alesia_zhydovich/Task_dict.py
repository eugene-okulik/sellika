# Создаем словарь my_dict с необходимыми ключами и значениями
my_dict = {
    'tuple': (1, 'cloud', 3, 4, 'cat', 6),
    'list': [10, 20, 'elephant', 40, 5.0],
    'dict': {'eye': 'blue', 'hair': 'short', 'hands': 2, 'legs': 4.3, 'e': 5},
    'set': {100, 200, 300, 400, 500}
}

# Для 'tuple' выводим последний элемент
print('Last element in tuple:', my_dict['tuple'][-1])

# Для 'list':
# Добавляем новый элемент в конец списка
my_dict['list'].append('carrot')
# Удаляем второй элемент (с индексом 1)
my_dict['list'].pop(1)

# Для 'dict':
# Добавляем элемент с ключом ('i am a tuple',)
my_dict['dict'][('i am a tuple',)] = "new"
# Удаляем какой-нибудь элемент
my_dict['dict'].pop('eye')

# Для 'set':
# Добавляем новый элемент в множество
my_dict['set'].add('Tima')
# Удаляем элемент из множества
my_dict['set'].remove(300)

# Выводим итоговый словарь
print('Result:')
print(my_dict)
