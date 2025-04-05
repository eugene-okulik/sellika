# Изначальное решение

# def repeat_me(func):
#     def wrapper(*args, **kwargs):
#         count = kwargs.pop('count')
#         for i in range(count):
#             func(*args, **kwargs)
#     return wrapper
#
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=3)

# Решение с фабрикой декораторов

def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me(count=10)
def example(text):
    print(text)

example('print me')
