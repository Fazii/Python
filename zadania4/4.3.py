def factorial(n):
    s = 1
    if n == 0:
        print("1 \n")
    else:
        while n > 0:
            s *= n
            n -= 1

    return s


print(factorial(5))
