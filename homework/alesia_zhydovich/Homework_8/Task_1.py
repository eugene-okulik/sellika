import random


salary = int(input('Укажи размер зарплаты: '))
bonus = random.choice([True, False])


def amount(salary, bonus):
    if bonus:
        bonus_amount = random.randrange(500, 10000, 100)
        salary += bonus_amount
        print(f'Бонус активен! Добавлено: {bonus_amount}')
    else:
        print('Бонус не активен.')
    print(f'Итоговая зарплата: ${salary}')


amount(salary, bonus)
