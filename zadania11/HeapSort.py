# -*- coding: iso-8859-2 -*-

""" Sortowanie przez kopcowanie (ang. heapsort) jest przykładem algorytmu sortowania danych.
    Jest stosunkowo niestabilny ale szybki i niepochłaniający wiele pamięci. Złożoność czasowa
    jest rzędu O(nlogn) z kolei zlożoność pamięciowa wynosi O(n). Algorytm wykorzystuje kolejkę priorytetową
    w postaci kopca binarnego. Sortowania przez kopcowanie składa się z dwóch faz. W pierwszej sortowane elemnty
    są reorganizowane w celu utworzenia kopca a w drugiej fazie dokonywane jest właściwe sortowanie.
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
