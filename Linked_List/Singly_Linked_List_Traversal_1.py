5# A simple Python Program for traversal of a Linkedlist

# Node Class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialise head
    def __init__(self):
        self.head = None


    # This function prints contents of linked list
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next



# Code execution starts heare
if __name__ == '__main__':

    # Start with teh empty list
    llist = LinkedList()

    # head node [1st node]
    llist.head = Node(10)

    # head next node [2nd node]
    llist.head.next = Node(20)

    # head next next next [4th node]
    llist.head.next.next.next = Node(40)

        # head next next node [3rd node]
    llist.head.next.next = Node(30)



    # printlist function call
    llist.printList()
