class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add_node(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_nodes(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


def create_linked_list():
    ll = LinkedList(5)
    ll.add_node(4)
    ll.add_node(3)
    ll.add_node(2)
    ll.add_node(1)
    return [ll, ll.head]


if __name__ == '__main__':
    l_l = create_linked_list()[0]
    l_l.print_nodes()
