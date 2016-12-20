import unittest


class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.head == self.tail:
            raise ValueError
        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data


class QueueTests(unittest.TestCase):

    def testIsEmpty(self):
        a = Queue()
        self.assertEqual(a.is_empty(), True)
        a.put(10)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.get(), 10)
        self.assertEqual(a.is_empty(), True)

    def testIsFull(self):
        a = Queue(3)
        self.assertEqual(a.is_full(), False)
        a.put(1)
        a.put(2)
        self.assertEqual(a.is_full(), False)
        a.put(4)
        self.assertEqual(a.is_full(), True)
        self.assertRaises(ValueError, lambda: a.put(55))

    def testPut(self):
        a = Queue(4)
        self.assertEqual(a.is_empty(), True)
        self.assertEqual(a.is_full(), False)
        a.put(5)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.is_full(), False)
        a.put(2)
        a.put(3)
        a.put(4)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.is_full(), True)
        self.assertRaises(ValueError, lambda: a.put(3))

    def testGet(self):
        a = Queue(2)
        self.assertRaises(ValueError, lambda: a.get())
        self.assertEqual(a.is_empty(), True)
        self.assertEqual(a.is_full(), False)
        a.put(4)
        a.put(6)
        self.assertEqual(a.is_empty(), False)
        self.assertEqual(a.is_full(), True)
        self.assertRaises(ValueError, lambda: a.put(2))
        self.assertEqual(a.get(), 4)
        self.assertEqual(a.get(), 6)
        self.assertRaises(ValueError, lambda: a.get())


if __name__ == '__main__':
    unittest.main()