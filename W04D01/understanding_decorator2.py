

def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before the function runs')
        func(*args, **kwargs)
        print('After the function runs')
    return wrapper


@greet_decorator
def say_hello(name):
    print(f"Hello {name}")


@greet_decorator
def add_the_no(a, b):
    print(a+b)


say_hello('Samjith')


add_the_no(1, 2)
