import operator
import time

Dict = {}
D = {}


def p(i, j):
    for i in range(i + 1):
        for j in range(j + 1):
            if i == 0 and j == 0:
                D[(i, j)] = 0.5
            elif i > 0 and j == 0:
                D[(i, j)] = 0
            elif i == 0 and j > 0:
                D[(i, j)] = 1
            else:
                D[(i, j)] = (D[(i - 1, j)] + D[(i, j - 1)]) / 2

    sorteddict = sorted(D.items(), key=operator.itemgetter(0))
    for k, v in sorteddict:
        print(k, ": ", v)
    print()


def prek(i, j):
    if i == 0 and j == 0:
        Dict[prek(0, 0)] = 0.5
        return 0.5
    elif i > 0 and j == 0:
        Dict['P(%d, 0)' % i] = 0
        return 0
    elif i == 0 and j > 0:
        Dict['P(0, %d)' % j] = 1
        return 1
    if j > 0 and i > 0:
        Dict['P(%d, %d)' % (i, j)] = (prek(i - 1, j) + prek(i, j - 1)) / 2
        return (prek(i - 1, j) + prek(i, j - 1)) / 2


def printRek():
    sorteddict = sorted(Dict.items(), key=operator.itemgetter(0))
    for k, v in sorteddict:
        print(k + " : ", v)


iter_begin = time.clock()
p(7, 3)
iter_end = time.clock()

rek_begin = time.clock()
prek(7, 3)
printRek()
rek_end = time.clock()

print("czas wykonania funkcji iteracyjnej   :", iter_end - iter_begin)
print("czas wykonania funkcji rekurencyjnej :", rek_end - rek_begin)
