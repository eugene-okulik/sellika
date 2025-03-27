def fibonacci():
    first = 0
    second = 1
    count = 1
    while count <= 100001:
        yield first
        first, second = second, first + second
        count += 1


index = [1, 5, 200, 1000, 100000]
index_num = 1
for num in fibonacci():
    if index_num in index:
        print(f"{index_num}-е число Фибоначчи: {num}")
    index_num += 1
    if index_num > max(index):
        break
