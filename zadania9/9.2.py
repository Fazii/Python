class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_node(node):
    print(node.data)


def print_list(node, visit):
    if node:
        visit(node)
        print_list(node.next, visit)


head1 = None
head1 = Node(1, head1)
head1 = Node(2, head1)
head1 = Node(3, head1)


head2 = None
head2 = Node(4, head2)
head2 = Node(5, head2)
head2 = Node(6, head2)

print("Lista 1")
print_list(head1, print_node)

print("Lista 2")
print_list(head2, print_node)


def get_last_node(node):
    while node.next:
        node = node.next
    return node


def merge(node1, node2):
    last1 = get_last_node(node1)
    last1.next = node2
    return node1

head3 = merge(head1, head2)

print("Lista 1+2")
print_list(head3, print_node)
