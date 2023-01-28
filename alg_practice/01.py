# Circular Linked List

# The Node class that contains data and next node
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node('head')    # At First, CLL starts with head node
        self.head.next = self.head  # when CLL creates first, it has just one node that is head

    # insert node
    def insert(self, item, new):
        new_node = Node(new)
        cur_node = self.find(item)
        new_node.next = cur_node.next
        cur_node.next = new_node

    # find data in CLL
    def find(self, item):
        cur_node = self.head
        while cur_node.element != item:
            cur_node = cur_node.next

        return cur_node

    # find previous node, because we need it when remove data in CLL
    def find_previous(self, item):
        cur_node = self.head
        while cur_node.next.element != item:
            cur_node = cur_node.next
        return cur_node

    # remove data in CLL
    def remove(self, item):
        prev_node = self.find_previous(item)
        prev_node.next = prev_node.next.next

    def show(self):
        cur_node = self.head
        while cur_node.next.element != 'head':
            print(cur_node.element, end=' -> ')
            cur_node = cur_node.next

        print(cur_node.element)


CLL01 = CircularLinkedList()
CLL01.insert('head', '1')
CLL01.insert('1', '2')
CLL01.insert('2', '3')
CLL01.insert('3', '4')
CLL01.show()
CLL01.remove('2')
CLL01.show()
