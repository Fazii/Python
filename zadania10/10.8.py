from collections import deque
import random


class RandomQueue:
    def __init__(self, size=5):
        self.container = deque()
        self.size = size

    def insert(self, item):
        if self.is_full():
            raise ValueError
        self.container.append(item)
        self.container.rotate(random.randint(-1, 1))

    def remove(self):
        if self.is_empty():
            raise ValueError
        self.container.rotate(random.randint(-1, 1))
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def is_full(self):
        return len(self.container) == self.size


kolejka = RandomQueue(6)
kolejka.insert(1)
kolejka.insert(2)
kolejka.insert(3)
kolejka.insert(4)
kolejka.insert(5)
kolejka.insert(6)

print(kolejka.remove())
print(kolejka.remove())
print(kolejka.remove())
print(kolejka.remove())
print(kolejka.remove())
