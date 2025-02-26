result1 = 'Результат операции: 42'
result2 = 'Результат операции: 514'
result3 = 'Результат работы программы: 9'

id1 = result1.index(":") + 2
id2 = result2.index(":") + 2
id3 = result3.index(":") + 2

number1 = int(result1[id1:]) + 10
number2 = int(result2[id2:]) + 10
number3 = int(result3[id3:]) + 10

print('Результат сложения:', number1)
print('Результат сложения:', number2)
print('Результат сложения:', number3)
