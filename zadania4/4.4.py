def fibonacci(n):
    if n <= 2:
        return 1
    else:
        f1, f2 = 1, 1
        for i in range(3, n+1):
            temp = f1 + f2
            f1 = f2
            f2 = temp

    return f2


print(fibonacci(10))
