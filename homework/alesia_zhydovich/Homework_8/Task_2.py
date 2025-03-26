def print_fibonacci(index):
    first = 0
    second = 1
    count = 1
    while count <= 100001:
        if count in index:
            print(f"{count}-е число Фибоначчи: {first}")
        first, second = second, first + second
        count += 1


index = [1, 5, 200, 1000, 100000]
print_fibonacci(index)
