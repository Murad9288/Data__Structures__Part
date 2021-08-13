'''
        # push()            Time complexity   : O(1)
                            Space complexity  : O(1)
                            
        # deleteNode()      Time complexity   : O(n)
                            space complexity  : O(1)
        # printList()       Time complexity   : O(n)
                            space complexity  : O(1)
'''



# A complete working prython3 program to deletion in singly linked list

# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linkedlist class
class Linkedlist:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        current_node = Node(new_data)
        current_node.next = self.head
        self.head = current_node


    # This function is DeleteNode
    def deleteNode(self, key):
        # Best Case
        if self.head is None:
            return

        # head node [1st node]
        if self.head.data == key:
            self.head = self.head.next
            return

        # Store head node
        # starting loop head.next node [2nd node]
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == key:
                current_node.next = current_node.next.next

            else:
                current_node = current_node.next

        return current_node


    # This function is printllist
    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next


# Driver program
if __name__ == '__main__':
    llist = Linkedlist()

    llist.push(9)
    llist.push(4)
    llist.push(2)
    llist.push(6)
    llist.push(7)

    # DeleteNode function call
    llist.deleteNode(2)

    # printllist function call
    llist.printlist()
