class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # traverse doublelinkedlist
    def print_doublylinkedlist(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.next

    # this is prepend function
    def prepend(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node
        self.size += 1

    # Add node doublelinkedlist end
    def append(self, new_data):
        # store new node
        node = Node(new_data)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def search(self, key):
        current_node = self.head
        if current_node is None or current_node.data == key:
            #return current_node.data
            return 'Yes'

        while current_node is not None:
            if current_node.data == key:
                #return current_node.data
                return 'Yes'

            current_node = current_node.next

        return 'sorry key is not found!'


    def remove(self, key):
        if self.head is None or self.head.data == key:
            self.head = self.head.next
            self.size -= 1
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == key:
                current_node.next = current_node.next.next
                self.size -= 1
            else:
                current_node = current_node.next
                self.tail = current_node

        return current_node


if __name__ == '__main__':
    dllist = DoublyLinkedlist()
    arr = [5, 1, 10, 3, 2]
    for i in arr:
        dllist.append(i)


    dllist.prepend(100)
    dllist.prepend(200)

    # call remove function
    dllist.remove(2)
    #dllist.remove(3)
    #dllist.remove(10)



    # call search function
    print(dllist.search(1))
    #print(dllist.search(500))
    print()


    # call double linkedlist remove function
    # call double linkedlist function
    print('Traverse Double linkedlist:')
    dllist.print_doublylinkedlist()
    print()

    print('\nhead->', dllist.head.data)
    print('tail->', dllist.tail.data)
    print('size->', dllist.size)
    print()
