'''
        # prepend()         Time complexity   : O(1)
                            Space complexity  : O(1)
        # insert()          Time complexity   : O(n)
                            space complexity  : O(1)
                            Worst case        : O(n)
                            Best case         : O(1)
                            Average case      : O(n/2)
                            
        # Append()          Time complexity   : O(n)
                            space complexity  : O(1)
'''

# insertion all methods of linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initilise next as null


# Linked List contains a Node object
class LinkedList:

    # Function to initialise head
    def __init__(self):
        self.head = None

    # This function is prepend
    def prepend(self, new_data):

        # Store new node
        current_node = Node(new_data)

        current_node.next = self.head
        self.head = current_node


    # This function is insert new node after the given prev_node.
    def insert(self, prev_none, new_data):

        # Store new node
        current_node = Node(new_data)

        # Best Case 1. check if the prev_node exists
        if  prev_none is None:
            print("The given prev_node must in Linked List")
            return


        current_node.next = prev_none.next
        prev_none.next = current_node


    # This function is append
    def Append(self, new_data):
        # Store new node
        current_node = Node(new_data)

        # Best Case 1. check if the head node empty or not empty
        if self.head is None:
            self.head = current_node
            return

        # Else traverse the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next


        # Change the next of last node
        last_node.next = current_node



    # This function is linkedlist print traversal\
    def printlist(self):

        # store the head node
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next



# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # llist-> append(2): 2
    llist.Append(2)

    # llist-> prepend(9): 9->2
    llist.prepend(9)

    # llist-> prepend(7): 7->9->2
    llist.prepend(7)

    # llist-> append(5): 7->9->2->5
    llist.Append(5)


    # llist-> # insert(10): 7->9->[10]->2->5
    #             7    9.next[ 10 ]
    prev = llist.head.next
    llist.insert(prev, 10)


    # This function is printlist
    print("Linked List Insertion:")
    llist.printlist()

