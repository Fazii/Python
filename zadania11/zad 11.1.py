import random


def randoml(size):
    if size < 1:
        raise ValueError
    l = []
    for i in range(size):
        num = random.randint(0, size - 1)
        l.append(num)
    return l


def nearRandoml(size):
    if size < 1:
        raise ValueError
    l = [x for x in range(size)]
    l.sort()
    for x in range(int(size / 10) + 1):
        pos = random.randint(0, size - 2)
        pos2 = random.randint(1, 2)
        poz2 = min(size - 1, pos + pos2)
        l[pos], l[poz2] = l[poz2], l[pos]
    return l


def reversedSortedl(size):
    if size < 1:
        raise ValueError
    l = nearRandoml(size)
    l.reverse()
    return l


def gaussl(size):
    return [round(random.gauss(size / 2, size / 6)) for _ in range(size)]


def setl(size, num):
    if num < 0 or size < 0:
        raise ValueError
    l = []
    for i in range(size):
        l.append(random.randint(0, num - 1))
    return l


print(randoml(17))
print(nearRandoml(11))
print(reversedSortedl(8))
print(gaussl(20))
print(setl(10, 7))
