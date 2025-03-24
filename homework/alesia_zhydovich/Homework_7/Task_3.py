results = [
    'Результат операции: 42',
    'Результат операции: 54',
    'Результат работы программы: 209',
    'Результат работы программы: 2'
]

def counting(result):
    element_id = result.index(":") + 2
    number = int(result[element_id:]) + 10
    print('Результат сложения:', number)

for element in results:
    counting(element)
