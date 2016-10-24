s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s2 = [15, 14, 13, 12, 11, 10, 9, 8, 7]

all = s1 + s2
total, repeated = set(), set()

for a in all:
    if a in total:
        repeated.add(a)
    else:
        total.add(a)

print('Sekwencja 1:'); print(s1)
print('Sekwencja 2:'); print(s2)
print('Powtarzajace sie elementy:'); print(repeated)
print('Wszystkie elementy:'); print(total)
