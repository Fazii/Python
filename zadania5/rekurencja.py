def factorial(n):
    s = 1
    if n == 0:
        print("1 \n")
    else:
        while n > 0:
            s *= n
            n -= 1

    return s


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        f1, f2 = 1, 1
        for i in range(3, n + 1):
            temp = f1 + f2
            f1 = f2
            f2 = temp

    return f2
