class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedlist:
    def __init__(self):
        self.head = None


    def print_doublylinkedlist_reverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def prepend(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node


    def reversed_doublylinkedlist(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


if __name__ == '__main__':
    dllist = DoublyLinkedlist()
    arr = [6, 2, 5, 7]
    for i in arr:
        dllist.prepend(i)

    print("This is doublylinkedlist:")
    dllist.print_doublylinkedlist_reverse()

    # Call reversed function
    dllist.reversed_doublylinkedlist()
    print('\nRreversed Doubly Linkedlist:')
    dllist.print_doublylinkedlist_reverse()
