def finished_me(func):
    def wrapper(*args):
        func(*args)
        print(f'{func.__name__} finished')
    return wrapper


@finished_me
def div(x, y):
    print(x / y)


div(81, 3)
