from math import gcd
import unittest
from fracs import *


class Frac:
    def __init__(self, x=0, y=1):
        if x % 1 == 0 and y % 1 == 0:
            if y == 0:
                raise ValueError("mianownik równy 0!")
            self.x = int(x)
            self.y = int(y)
        elif isinstance(x, float):
            args = x.as_integer_ratio()
            self.x = int(args[0])
            self.y = int(args[1])
        elif isinstance(x, int):
            self.x = x
            self.y = y
        else:
            raise ValueError("Podano błędny typ argumentu")


    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + '/' + str(self.y)

    def __repr__(self):
        return "Frac(%s, %s)" % (self.x, self.y)

    def __cmp__(self, other):
        other = self.otherToFrac(other)
        subtract = self - other
        if subtract.x == 0:
            return 0
        if subtract.x * subtract.y > 0:
            return 1
        else:
            return -1

    def __add__(self, other):
        other = self.otherToFrac(other)
        multiple = int(self.y * other.y / gcd(self.y, other.y))
        result = [int(self.x * multiple / self.y + other.x * multiple / other.y), multiple]
        divider = gcd(result[0], result[1])
        return Frac(result[0] / divider, result[1] / divider)

    __radd__ = __add__

    def __sub__(self, other):
        other = self.otherToFrac(other)
        return self + (-other)

    def __rsub__(self, other):
        other = self.otherToFrac(other)
        return other - self

    def __mul__(self, other):
        other = self.otherToFrac(other)
        result = [self.x * other.x, self.y * other.y]
        divider = gcd(result[0], result[1])
        return Frac(result[0] / divider, result[1] / divider)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.otherToFrac(other)
        return self * ~other

    def __rtruediv__(self, other):
        other = self.otherToFrac(other)
        return other / self

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):  # konwersja do float
        return float(self.x) / float(self.y)

    def __eq__(self, other):
        other = self.otherToFrac(other)
        sub = self - other
        if sub.x == 0:
            return True
        else:
            return False

    def __lt__(self, other):
        other = self.otherToFrac(other)
        sub = self - other
        if sub.x * sub.y >= 0:
            return False
        else:
            return True

    def __gt__(self, other):
        other = self.otherToFrac(other)
        sub = self - other
        if sub.x * sub.y > 0:
            return True
        else:
            return False

    def __le__(self, other):
        other = self.otherToFrac(other)
        sub = self - other
        if sub.x * sub.y > 0:
            return False
        else:
            return True

    def __ge__(self, other):
        other = self.otherToFrac(other)
        sub = self - other
        if sub.x * sub.y >= 0:
            return True
        else:
            return False

    def otherToFrac(self, x):
        if isinstance(x, Frac):
            return x
        elif isinstance(x, float) or isinstance(x, int):
            return Frac(x)
        else:
            raise ValueError("Podano błędny typ argumentu")


class TestFractions(unittest.TestCase):
    def test_eq_frac(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertFalse(Frac(5, 3) == Frac(10, 2))
        self.assertTrue(Frac(1, 2) == 0.50)
        self.assertTrue(Frac(3, 1) == 3)
        self.assertTrue(2 == Frac(2, 1))
        self.assertFalse(Frac(0, 2) == 3)
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Frac(1, 2) == "xyz"

    def test_neq_frac(self):
        self.assertTrue(Frac(1, 2) != Frac(1, 3))
        self.assertFalse(Frac(1, 3) != Frac(2, 6))
        self.assertFalse(Frac(1, 2) != 0.50)
        self.assertFalse(Frac(12, 4) != 3)
        self.assertTrue(Frac(5, 2) != 2)



    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 2), Frac(1, 1))
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertNotEqual(Frac(3, 4) + Frac(2, 5), Frac(2, 1))
        self.assertEqual(0.5 + Frac(1, 2), 1)
        self.assertEqual(2 + 2, 4)
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Frac(1, 2) + "xyz"

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 2) - 0.5, 0)
        self.assertEqual(Frac(1, 2) - 1, -0.5)
        self.assertEqual(Frac(3, 2) + 1, Frac(5, 2))
        self.assertEqual(1 - Frac(3, 2), Frac(-1, 2))
        self.assertEqual(Frac(10, 30) - Frac(1, 3), Frac(0, 1))
        self.assertEqual(Frac(12, 30) - Frac(1, 3), Frac(1, 15))
        self.assertNotEqual(Frac(12, 30) - Frac(1, 3), Frac(1, 16))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Frac(1, 2) - "xyz"

    def test_mul_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(2, 4) * Frac(2, 6), Frac(1, 6))
        self.assertEqual(Frac(1, 4) * 2, 0.50)
        self.assertEqual(Frac(1, 10) * 10, Frac(1, 1))
        self.assertEqual(10 * Frac(1, 3), Frac(10, 3))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Frac(1, 2) * "xyz"

    def test_div_frac(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 2), 1)
        self.assertEqual(Frac(12, 30) / Frac(2, 6), Frac(6, 5))
        self.assertEqual(3 / Frac(1, 2), Frac(6, 1))
        self.assertEqual(Frac(12, 30) / 3, Frac(2, 15))
        self.assertEqual(0.5 / 3, Frac(1, 6))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Frac(1, 2) / "xyz"

    def test_frac2float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(1, 4)), 0.25)
        self.assertNotEqual(float(Frac(3, 8)), 0.370)

    def test_gt_frac(self):
        self.assertTrue(Frac(1, 2) > Frac(1, 4))
        self.assertFalse(Frac(5, 16) > Frac(2, 5))
        self.assertTrue(1 > Frac(2, 6))
        self.assertTrue(0.5 > Frac(2, 6))
        self.assertFalse(0.5 > Frac(2, 3))

    def test_lt_frac(self):
        self.assertFalse(Frac(1, 2) < Frac(1, 4))
        self.assertFalse(Frac(5, 10) < Frac(2, 6))
        self.assertTrue(Frac(6, 18) < 0.5)
        self.assertTrue(Frac(4, 8) < 1)
        self.assertTrue(Frac(3, 10) < Frac(3, 4))
        self.assertTrue(0.4 < Frac(3, 6))

    def test_le_frac(self):
        self.assertFalse(Frac(1, 2) <= Frac(1, 4))
        self.assertTrue(Frac(3, 8) <= Frac(5, 6))
        self.assertTrue(Frac(1, 2) <= Frac(2, 4))

    def test_ge_frac(self):
        self.assertTrue(Frac(1, 2) >= Frac(1, 4))
        self.assertTrue(Frac(3, 8) >= Frac(1, 6))
        self.assertFalse(Frac(1, 2) >= Frac(2, 3))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()