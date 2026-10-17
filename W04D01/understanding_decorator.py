
# This is a decorator, and it can be used above other functions that you have.
def greet_decorator(func):
    def wrapper():
        print('Before the function runs')
        func()
        print('After the function runs')
    return wrapper


@greet_decorator
def say_hello():
    print("Hello PYMD060926")

say_hello()
