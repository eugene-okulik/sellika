first = int(input('Text first number: ' ))
second = int(input('Text second number: ' ))


def operation_selector(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@operation_selector
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


result = calc(first, second)
print('Result:', result)
