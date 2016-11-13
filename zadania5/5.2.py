import math
import unittest


def add_frac(frac1, frac2):
    tmpfrac1 = frac1[1]
    frac1[0] = frac1[0] * frac2[1]
    frac1[1] = tmpfrac1 * frac2[1]

    frac2[0] = frac2[0] * tmpfrac1
    frac2[1] = frac1[1]

    a = frac1[0] + frac2[0]
    b = frac1[1]
    gcd = math.gcd(a, b)
    if gcd != 1:
        a /= gcd
        b /= gcd
    result = [a, b]
    return result


def sub_frac(frac1, frac2):
    tmpfrac1 = frac1[1]
    frac1[0] = frac1[0] * frac2[1]
    frac1[1] = tmpfrac1 * frac2[1]

    frac2[0] = frac2[0] * tmpfrac1
    frac2[1] = frac1[1]

    a = frac1[0] - frac2[0]
    b = frac1[1]
    gcd = math.gcd(a, b)
    if gcd != 1:
        a /= gcd
        b /= gcd
    result = [a, b]
    return result


def mul_frac(frac1, frac2):
    a = frac1[0] * frac2[0]
    b = frac1[1] * frac2[1]
    gcd = math.gcd(a, b)
    if gcd != 1:
        a /= gcd
        b /= gcd
    result = [a, b]
    return result


def div_frac(frac1, frac2):
    a = frac1[0] * frac2[1]
    b = frac1[1] * frac2[0]
    gcd = math.gcd(a, b)
    if gcd != 1:
        a /= gcd
        b /= gcd
    result = [a, b]
    return result


def is_positive(frac):
    if (frac[0] >= 0 and frac[1] < 0) or (frac[0] < 0 and frac[1] > 0):
        return False
    else:
        return True


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    tmpfrac1 = frac1[1]
    frac1[0] = frac1[0] * frac2[1]
    frac1[1] = tmpfrac1 * frac2[1]

    frac2[0] = frac2[0] * tmpfrac1
    frac2[1] = frac1[1]

    if frac1[0] == frac2[0]:
        return 0
    elif frac1[0] > frac2[0]:
        return 1
    else:
        return -1


def frac2float(frac):
    return frac[0] / frac[1]


f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 2], [1, 1]), [2, 1])
        self.assertEqual(add_frac([10, 2], [10, 5]), [7, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([2, 2], [1, 1]), self.zero)
        self.assertEqual(sub_frac([10, 2], [10, 5]), [3, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 2], [1, 1]), [1, 1])
        self.assertEqual(mul_frac([10, 2], [10, 5]), [10, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([2, 2], [1, 1]), [1, 1])
        self.assertEqual(div_frac([10, 2], [10, 5]), [5, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([2, 1]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([0, -2]), True)
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([1, -2]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 4], [1, 3]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([-1, 2]), -0.5)

    def tearDown(self):
        self.zero = None


if __name__ == '__main__':
    unittest.main()
