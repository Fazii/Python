def odwracanie(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    if left + 1 != right:
        odwracanie(L, left + 1, right - 1)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie(L, 3, 7)
print(L)


def odwracanie(L, left, right):
    if left >= right:
        return
    for i in range(int((right - left) / 2)):
        L[left + i], L[right - i] = L[right - i], L[left + i]


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie(L, 3, 7)
print(L)
