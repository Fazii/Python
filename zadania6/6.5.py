import unittest
from math import gcd


class Frac:
    def __init__(self, x=0, y=1):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + '/' + str(self.y)

    def __repr__(self):
        return "Frac(%s, %s)" % (self.x, self.y)

    def __add__(self, other):
        lcm = int(self.y * other.y / gcd(self.y, other.y))
        ret = [int(self.x * lcm / self.y + other.x * lcm / other.y), lcm]
        divider = gcd(ret[0], ret[1])
        return Frac(ret[0] / divider, ret[1] / divider)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        ret = [self.x * other.x, self.y * other.y]
        divider = gcd(ret[0], ret[1])
        return Frac(ret[0] / divider, ret[1] / divider)

    def __truediv__(self, other):
        return self * ~other

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __cmp__(self, other):
        sub = self - other
        if sub.x == 0:
            return 0
        elif sub.x * sub.y > 0:
            return 1
        else:
            return -1

    def __eq__(self, other):
        sub = self - other
        if sub.x == 0:
            return True
        else:
            return False

    def __neq__(self, other):
        if self == other:
            return False
        else:
            return True

    def __lt__(self, other):
        sub = self - other
        if sub.x * sub.y >= 0:
            return False
        else:
            return True

    def __gt__(self, other):
        sub = self - other
        if sub.x * sub.y > 0:
            return True
        else:
            return False

    def __le__(self, other):
        sub = self - other
        if sub.x * sub.y > 0:
            return False
        else:
            return True

    def __ge__(self, other):
        sub = self - other
        if sub.x * sub.y >= 0:
            return True
        else:
            return False

    def __float__(self):
        return float(self.x) / float(self.y)


class TestFractions(unittest.TestCase):
    def setUp(self):
        pass

    def test_eq_frac(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertFalse(Frac(1, 18) == Frac(2, 6))

    def test_neq_frac(self):
        self.assertTrue(Frac(1, 2) != Frac(1, 4))
        self.assertFalse(Frac(6, 18) != Frac(2, 6))

    def test_gt_frac(self):
        self.assertTrue(Frac(1, 2) > Frac(1, 4))
        self.assertFalse(Frac(6, 18) > Frac(2, 6))

    def test_lt_frac(self):
        self.assertFalse(Frac(1, 2) < Frac(1, 4))
        self.assertFalse(Frac(6, 18) < Frac(2, 6))
        self.assertTrue(Frac(6, 18) < Frac(3, 6))

    def test_le_frac(self):
        self.assertFalse(Frac(1, 2) <= Frac(1, 4))
        self.assertTrue(Frac(6, 18) <= Frac(2, 6))
        self.assertTrue(Frac(6, 18) <= Frac(3, 6))

    def test_ge_frac(self):
        self.assertTrue(Frac(1, 2) >= Frac(1, 4))
        self.assertTrue(Frac(6, 18) >= Frac(2, 6))
        self.assertFalse(Frac(6, 18) >= Frac(3, 6))

    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(3, 10) + Frac(1, 3), Frac(19, 30))

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(12, 30) - Frac(1, 3), Frac(1, 15))

    def test_mul_frac(self):
        self.assertEqual(Frac(22, 2) * Frac(1, 12), Frac(11, 12))
        self.assertEqual(Frac(12, 30) * Frac(1, 3), Frac(2, 15))

    def test_div_frac(self):
        self.assertEqual(Frac(22, 2) / Frac(7, 12), Frac(132, 7))
        self.assertEqual(Frac(12, 30) / Frac(1, 3), Frac(6, 5))

    def test_is_positive(self): pass

    def test_frac2float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(3, 8)), 0.375)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
