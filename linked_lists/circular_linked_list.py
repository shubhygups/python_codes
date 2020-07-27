import os
import sys

sys.path.insert(0, os.path.abspath('.'))
from basic_linked_list import create_linked_list


def find_circular(head):
    first = head
    if head.next:
        second = head.next.next
    else:
        second = head.next

    while first and second and first != second:
        if first == second:
            print("Loop Found")
        first = first.next
        if second.next:
            second = second.next.next
        else:
            second = second.next

    if not first or not second:
        print("Loop not found")
    return


if __name__ == '__main__':
    l_l = create_linked_list()
    l_l[0].add_node(0)
    temp_head = l_l[1]
    link_node = None
    while temp_head.next is not None:
        if temp_head.data == 3:
            link_node = temp_head
        temp_head = temp_head.next
    temp_head.next = link_node
    find_circular(l_l[1])
    # l_l[0].print_nodes()
