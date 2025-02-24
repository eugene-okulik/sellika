import math

number_1 = float(input('Text first number, 1: '))
number_2 = float(input('Text second number, 2: '))

arithmetic_mean = (number_1 + number_2) / 2
geometric_mean = math.sqrt(number_1 * number_2)

# geometric_mean = (number_1 * number_2) ** 0.5  если решать без импорта модуля math

print('Arithmetic_mean: ', arithmetic_mean)
print('Geometric_mean: ', geometric_mean)
