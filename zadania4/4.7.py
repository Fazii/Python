def flatten(sequence):
    L = []
    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            L.extend(flatten(sequence[i]))
        else:
            L.append(sequence[i])
    return L


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
