def inv_decorator(func):
    def wrapper(*args):
        a = []
        for i in range (len(args)-1,-1,-1):
            a.append(args[i])
        return func(*a)
    return wrapper

@inv_decorator
def foo(*a):
    for i in a:
        print(i, end=' ')
foo(1,2,3,543)