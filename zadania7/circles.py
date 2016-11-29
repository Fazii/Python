import unittest
from collections.__main__ import Point
from math import pi
from circles import *


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("Promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle(%s, %s, %s)" % (self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Podano błędny typ argumentu")
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * self.radius * self.radius

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Podano błędny typ argumentu")
        r = max((self.radius + other.radius + (other.pt - self.pt).length()) / 2, self.radius, other.radius)
        temp = (r - self.radius) / (2 * r - self.radius - other.radius)
        x = self.pt.x + temp * (other.pt.x - self.pt.y)
        y = self.pt.y + temp * (other.pt.y - self.pt.y)
        return Circle(x, y, r)


class TestCircles(unittest.TestCase):
    def test_init_circles(self):
        with self.assertRaisesRegex(ValueError, "Promień ujemny"):
            Circle(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Circle(1, 1, "xyz")

    def test_eq_circles(self):
        self.assertTrue(Circle(1, 2, 5) == Circle(1, 2, 5))
        self.assertTrue(Circle(1, 2, 5) == Circle(1.0, 2.0, 5))
        self.assertFalse(Circle(1, 3) == Circle(3, 1))
        self.assertTrue(Circle(1, 3) == Circle(1, 3))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Circle(1, 1) == "xyz"

    def test_ne_circles(self):
        self.assertFalse(Circle(1, 2) != Circle(1, 2))
        self.assertFalse(Circle(1, 2) != Circle(1.0, 2.0))
        self.assertTrue(Circle(1, 3) != Circle(3, 1))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Circle(1, 5) == "xyz"

    def test_area_circles(self):
        self.assertEqual(Circle(1, 1, 1).area(), pi)
        self.assertEqual(Circle(1, 1, 2).area(), 4 * pi)

    def test_move_circles(self):
        self.assertEqual(Circle(1, 1).move(0, 0), Circle(1, 1))
        self.assertEqual(Circle(1, 1).move(1, 2), Circle(2, 3))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Circle(1, 1).move("xyz", 1)

    def test_cover_circles(
            self):
        self.assertEqual(Circle(1, 1, 1).cover(Circle(3, 1, 1)), Circle(2, 1, 2))
        self.assertEqual(Circle(1, 1, 1).cover(Circle(1, 5, 2)), Circle(1, 3.5, 3.5))
        self.assertEqual(Circle(1, 1, 1).cover(Circle(2, 1, 5)), Circle(2, 1, 5))
        with self.assertRaisesRegex(ValueError, "Podano błędny typ argumentu"):
            Circle(0, 0, 1).cover("xyz")

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
