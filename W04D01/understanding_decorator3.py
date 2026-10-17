
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for no in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(n=5)
def say_hello():
    print("Hello PYMD060926")

say_hello()
