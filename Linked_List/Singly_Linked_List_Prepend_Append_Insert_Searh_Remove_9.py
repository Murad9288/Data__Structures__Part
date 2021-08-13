'''
        # printllist()      Time complexity   : O(n)
                            space complexity  : O(1)
        # push()            Time complexity   : O(1)
                            Space complexity  : O(1)
        # append()          Time complexity   : O(n)
                            space complexity  : O(1)
        # prepend()         Time complexity   : O(1)
                            space complexity  : O(1)
        # searching()       Time complexity   : O(n)
                            space complexity  : O(1)
        # inserting()       Time complexity   : O(n)
                            space complexity  : O(1)
        # remove()          Time complexity   : O(n)
                            space complexity  : O(1)
'''

# Node class
class Node:
    def __init__(self,data=None, next=None):
        self.data = data # Assign data
        self.next = next # Initialize next as null


# Linked List class contains a Node object
class Linkedlist:
    def __init__(self):

        # Function to initialize head
        self.head = None

    # linked list traverse
    def printllist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


    # linked list Insert at the end
    def append(self, data):
        current_node = Node(data)
        if self.head == None:
            self.head = current_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = current_node


    # linked list Insert after a node
    def prepend(self, data):
        current_node = Node(data)
        current_node.next = self.head
        self.head = current_node

        # linked list Insert at the beginning
    def inserting(self, prev, new_data):
        if prev is None:
            print('The given previous node must in LinkedList.')
            return

        node = Node(new_data)
        node.next = prev.next
        prev.next = node



    # linked list searching node
    def searching(self, key):
        if self.head is None:
            return False

        if self.head.data == key:
            return True

        current = self.head.next
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        else:
            return False


    # linked list remove node.
    def remove(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next

            else:
                current = current.next

        return current




# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = Linkedlist()
    llist.append('a')
    llist.append('d')
    llist.prepend('1')
    llist.append(100)
    print("Print Linkedlist:")
    llist.printllist()
    print('\n')

    #inserting
    print("Insert Node:->Murad")
    llist.inserting(llist.head.next.next, 'Murad')
    llist.printllist()
    print('\n')

    #remove
    print("Remove Node:-> 100")
    llist.remove(100)
    llist.printllist()
    print('\n')

    #searching
    print('Searching Node:-> 1')
    if llist.searching('1'):
        print("Yes")
    else:
        print("No")
