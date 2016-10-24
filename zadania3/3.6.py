from pip._vendor.distlib.compat import raw_input


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


try:
    print('Podaj liczbe kratek w poziomie')
    x = int(raw_input())
    print('Podaj liczbe kratek w pionie')
    y = int(raw_input())
except ValueError:
    print('Bledny parametr')
    exit()

out = horizontalline(x) + "\n"
for i in range(y):
    out += verticalline(x) + "\n" + horizontalline(x) + "\n"

print(out)
