def solve1(a,b,c):
    if a == 0 and b == 0:
        if c == 0:
            print("Równanie jest nieokreślone.")
            return
        else:
            print("Równanie sprzeczne.")
            return
    if a == 0:
        print("Rozwiązanie y = "+str(-float(c)/float(b)))
        return
    if b == 0:
        print("Rozwiązanie x = "+str(-float(c)/float(a))+" i y e R")
        return
    s = str(float(-c)/float(b))+"+("+str(float(-a)/float(b))+")x"
    print("Rozwiązanie y = "+s+", zbiór punktów o wzorze (y, "+s+")")


solve1(0, 0, 0)
solve1(0, 0, 1)
solve1(0, 2, 0)
solve1(0, 2, 2)
solve1(2, 0, 0)
solve1(2, 0, 2)
solve1(2, 1, 0)
solve1(2, 1, -3)
