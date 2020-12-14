def fib(n):
    if n < 0:
        raise ValueError('Value cannot be less than zero.')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(3))
