# -*- coding: iso-8859-2 -*-

""" Sortowanie przez kopcowanie (ang. heapsort) jest przyk�adem algorytmu sortowania danych.
    Jest stosunkowo niestabilny ale szybki i niepoch�aniaj�cy wiele pami�ci. Z�o�ono�� czasowa
    jest rz�du O(nlogn) z kolei zlo�ono�� pami�ciowa wynosi O(n). Algorytm wykorzystuje kolejk� priorytetow�
    w postaci kopca binarnego. Sortowania przez kopcowanie sk�ada si� z dw�ch faz. W pierwszej sortowane elemnty
    s� reorganizowane w celu utworzenia kopca a w drugiej fazie dokonywane jest w�a�ciwe sortowanie.
"""


def heapsort(l):
    for start in range(int((len(l) - 2) / 2), -1, -1):
        siftdown(l, start, len(l) - 1)
    for end in range(len(l) - 1, 0, -1):
        l[end], l[0] = l[0], l[end]
        siftdown(l, 0, end - 1)
    return l


def siftdown(l, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and l[child] < l[child + 1]:
            child += 1
        if l[root] < l[child]:
            l[root], l[child] = l[child], l[root]
            root = child
        else:
            break


l = [1, 2, 3, -3, -2, -1, 0]
heapsort(l)
print(l)
