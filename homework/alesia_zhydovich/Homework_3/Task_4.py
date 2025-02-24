import math

a = float(input ('Text first cathetus, a: '))
b = float(input ('Text second cathetus, b: '))

hypotenuse = math.sqrt(a**2 + b**2)
area = (a * b) / 2

print('Hypotenuse: ', hypotenuse)
print('Area: ', area)