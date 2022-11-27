def fib(n):
    x, y = 0, 1
    for __ in range(n):
        yield x
        x, y = y, x + y

print(list(fib(10)))