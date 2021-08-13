# Python program to swap two given nodes of a linked list
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        current_node = Node(new_data)
        current_node.next = self.head
        self.head = current_node

    # Function to swap Nodes x and y in linked list by
    def swapNodes(self, x, y):
        if x == y:
            return

        current_node = self.head
        while current_node:
            if current_node.data == x:
                current_node.data = y

            elif current_node.data == y:
                current_node.data = x

            current_node = current_node.next



    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

if __name__ == '__main__':
    # 1->2->3->4->5
    llist = Linkedlist()
    li = [5, 4, 3, 2, 1]
    for i in li:
        llist.push(i)

    print("Linked list before calling swapNodes():")
    llist.printlist()

    print("\nLinked list after calling swapNodes():")
    llist.swapNodes(2, 5)
    llist.printlist()
