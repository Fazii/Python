import math
import random


def calc_pi(n):
    ctr = 0
    for i in range(n):
        if math.pow(random.random(), 2.0) + math.pow(random.random(), 2.0) <= 1.0:
            ctr += 1
    print(4.0 * ctr / n)


calc_pi(1000000)
