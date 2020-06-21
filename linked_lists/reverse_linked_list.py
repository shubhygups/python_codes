import os
import sys

sys.path.insert(0, os.path.abspath('.'))
from basic_linked_list import create_linked_list


def reverse_linked_list(head):
    first = head
    second = head.next

    first.next = None
    while second is not None:
        temp = second.next
        second.next = first
        first = second
        second = temp
    head = first
    return head


if __name__ == '__main__':
    l_l = create_linked_list()
    l_l[0].head = reverse_linked_list(l_l[1])
    l_l[0].print_nodes()
