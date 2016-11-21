import unittest
from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)


class TestPoints(unittest.TestCase):

    def setUp(self): pass

    def test_str_frac(self):
        self.assertEqual(str(Point(55, 22)), "(55, 22)")

    def test_eq_frac(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(2, 2) == Point(1, 2))

    def test_ne_frac(self):
        self.assertFalse(Point(1, 2) != Point(1, 2))
        self.assertTrue(Point(2, 2) != Point(1, 2))

    def test_add_frac(self):
        self.assertEqual(Point(55, 22) + Point(3, 7), Point(58, 29))

    def test_sub_frac(self):
        self.assertEqual(Point(55, 22) - Point(3, 7), Point(52, 15))

    def test_mul_frac(self):
        self.assertEqual(Point(2, 3) * Point(3, 8), 30)

    def test_cross_frac(self):
        self.assertEqual(Point(2, 3).cross(Point(3, 8)), 7)

    def test_length_frac(self):
        self.assertEqual(Point(3, 4).length(), 5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
