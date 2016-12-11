import unittest


class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_total(top):
    if top is None:
        return 0
    return count_total(top.left) + top.data + count_total(top.right)


def count_leafs(top):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return count_leafs(None) + 1 + count_leafs(None)
    else:
        return count_leafs(top.left) + count_leafs(top.right)


class TestNode(unittest.TestCase):

    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.right.left.left = Node(10)

        self.root1 = Node(5)

        self.root2 = None

    def test_count_leafs(self):
        self.assertTrue(count_leafs(self.root) == 4)
        self.assertTrue(count_leafs(self.root1) == 1)
        self.assertTrue(count_leafs(self.root2) == 0)

    def test_count_total(self):
        self.assertTrue(count_total(self.root) == 38)
        self.assertTrue(count_total(self.root1) == 5)
        self.assertTrue(count_total(self.root2) == 0)
