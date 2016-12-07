import math


def heron(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError
    p = 0.5*(a+b+c)
    print(math.sqrt(p*(p-a)*(p-b)*(p-c)))


try:
    heron(3, 4, 5)
    heron(1, 2, 7)
except ValueError:
     print("Wartości nie spełniają nierówności trójkąta!")