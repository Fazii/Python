import math

from pip._vendor.distlib.compat import raw_input

print('Podaj dlugosc miarki')
try:
    long = int(raw_input())
except ValueError:
    print('Bledny parametr')
    exit()

s = "|"
for i in range(1, long + 1):
    s += "....|"
s += "\n0"
for i in range(1, long + 1):
    for j in range(4 - int(math.floor(math.log(i, 10)))):
        s += ' '
    s += str(i)

print(s)
