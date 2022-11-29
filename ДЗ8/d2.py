def print_decorator(func):
    def wrapper(*args):
        res = func(*args)
        print(args)
        return res
    return wrapper

@print_decorator
def foo(*A):
    for i in A:
        print(i*2+1, end=' ')
    print(end='\n')
foo(1,2,3,4,5)