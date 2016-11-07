def sum_seq(sequence):
    s = 0
    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            s += sum_seq(sequence[i])
        else:
            s += sequence[i]

    return s

sequence = [(0), 1, [2, 3], (4, 5), [(6, 7), 8], ([9, 10], 11)]
print(sum_seq(sequence))