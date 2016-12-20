import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n >= self.size:
            raise ValueError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise ValueError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data


class StackTests(unittest.TestCase):

    def testIsEmpty(self):
        a = Stack()
        self.assertEqual(a.is_empty(), True)
        a.push(3)
        self.assertEqual(a.is_empty(), False)
        a.pop()
        self.assertEqual(a.is_empty(), True)

    def testIsFull(self):
        a = Stack()
        self.assertEqual(a.is_full(), False)
        for i in range(a.size):
            a.push(i)
        self.assertEqual(a.is_full(), True)
        a.pop()
        self.assertEqual(a.is_full(), False)
        a.push(3)
        self.assertEqual(a.is_full(), True)

    def testPush(self):
        a = Stack(4)
        self.assertEqual(a.is_empty(), True)
        self.assertEqual(a.is_full(), False)
        a.push(5)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.is_full(), False)
        a.push(7)
        a.push(8)
        a.push(9)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.is_full(), True)
        self.assertRaises(ValueError, lambda: a.push(3))

    def testPop(self):
        a = Stack(2)
        self.assertRaises(ValueError, lambda: a.pop())
        self.assertEqual(a.is_empty(), True)
        self.assertEqual(a.is_full(), False)
        a.push(4)
        a.push(6)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.is_full(), True)
        self.assertEqual(a.pop(), 6)
        self.assertEqual(a.pop(), 4)


if __name__ == '__main__':
    unittest.main()
