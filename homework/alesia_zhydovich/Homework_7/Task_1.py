number = 4

while True:
    user_input = int(input("Угадайте число: "))
    if user_input == number:
        print("Поздравляю! Вы угадали!")
        break
    elif user_input != number:
        print("Попробуйте снова")
        continue
