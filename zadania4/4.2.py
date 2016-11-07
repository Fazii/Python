import math


def measure(long):
    s = "|"
    for i in range(1, long + 1):
        s += "....|"
    s += "\n0"
    for i in range(1, long + 1):
        for j in range(4 - int(math.floor(math.log(i, 10)))):
            s += ' '
        s += str(i)
    return s


def horizontalline(n):
    s = "+"
    for i in range(n):
        s += "---+"
    return s


def verticalline(n):
    s = "|"
    for i in range(n):
        s += "   |"
    return s


def rectangle(x, y):
    wy = horizontalline(x) + "\n"
    for i in range(y):
        wy += verticalline(x) + "\n" + horizontalline(x) + "\n"
    return wy

print(measure(12) + "\n")
print(rectangle(4, 2))
