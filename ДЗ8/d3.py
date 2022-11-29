def error_decorator(func):
    def wrapper(a,b):
        try:
            func(a,b)
        except BaseException:
            return 'error'
        return func(a,b)
    return wrapper

@error_decorator
def foo(x,y):
    return x/y

print(foo(1,2))
print(foo(1,0))