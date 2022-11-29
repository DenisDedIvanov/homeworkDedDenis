import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        t=time.time() - start_time
        return res,t
    return wrapper

@time_decorator
def Fib_dinamic(n):
    if n<1:
        return
    A=[0, 1]+[0]*(n-1)
    for i in range(2, n+1):
        A[i] = A[i-1] + A[i-2]
    return A[n-1]

def Fib_recursion(n):
        if n <= 1:
            return n
        return Fib_recursion(n - 1) + Fib_recursion(n - 2)

@time_decorator
def fib_recursion(n):
    return Fib_recursion(n)

res1, t1=fib_recursion(30)
res2, t2=Fib_dinamic(30)
print('Рекурсия: ',t1, ' с, цикл:',t2, 'с')