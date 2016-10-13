# 2.10

line = 'ab\tcd\nef\n\gh\t\nij'.split()
lenght = len(line)
print(lenght)

del line, lenght

# 2.11

line = 'word'
S1 = list()
S = [x for x in line]
for x in S:
    S1.append(x + "_")
S1 = ''.join(S1)
print(S1)

del line, S1, S

# 2.12

line = 'ab cd ef gh ij kl'
S1 = list()
S2 = list()
S = line.split()
for x in range(0, len(S)):
    S1.append(S[x][0])
    S2.append(S[x][-1:])
S1 = ''.join(S1)
S2 = ''.join(S2)
print(S1)
print(S2)

del line, S1, S2, S

# 2.13

line = 'ab\tcd\nef gh\t\nij aaa bbb'.split()
S = sum(len(x) for x in line)
print(S)

del line, S

# 2.14

line = 'a bb ccc dddd eeeee ffff ggg hh i'.split()
line.sort(key=len, reverse = True)
S = line[0]
S1 = len(line[0])
print(S)
print(S1)

del line, S, S1

# 2.15

L = [1,2,3,4,5,6,7,8,9]
L = ''.join(str(x) for x in L)
print(L)

del L

# 2.16

line = 'aa bb GvR bb aa cc'
line = line.replace('GvR', 'Guido van Rossum')
print(line)

del line

# 2.17

line = 'a ab bacd cecc ddeee edeeeede aaaabba'
line = line.split()
line.sort()
line = ' '.join(line)
print(line)
line = line.split()
line.sort(key=len)
line = ' '.join(line)
print(line)

del line

# 2.18

line = 123456780098734567809097660707097987079870
S = str(line)
S1 = S.count('0')
print(S1)

del line, S, S1

# 2.19

line = [1, 22, 333, 4, 55, 666, 7, 88, 999]
line1 = []
for x in line:
    line1.append(str(x).zfill(3))
line1 = ' '.join(line1)
print(line1)

