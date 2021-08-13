'''
    Merge two sorted linked lists
    Time Complexity     :
    Space Complexity    :
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')

            current_node = current_node.next

    def addTwolist(self, new_data):
        current_node = Node(new_data)
        if self.head is None:
            self.head = current_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = current_node


def mergeSort(A_head, B_head):
    if A_head is None:
        return B_head

    if B_head is None:
        return A_head


    if A_head.data < B_head.data:
        A_head.next = mergeSort(A_head.next, B_head)
        return A_head

    else:
        B_head.next = mergeSort(B_head.next, A_head)
        return B_head


if __name__ == '__main__':
    # Create 2 lists
    listA = Linkedlist()
    listB = Linkedlist()

    # Add elements to the list in sorted order
    listA.addTwolist(2)
    listA.addTwolist(4)
    listA.addTwolist(7)

    listB.addTwolist(1)
    listB.addTwolist(3)
    listB.addTwolist(20)

    listA.head = mergeSort(listA.head, listB.head)

    print("Merge two sorted linked lists:")

    listA.printlist()

"""
#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def sortedMerge(head_A, head_B):
    # code here
    dummyNode = Node(0)
    tail = dummyNode
    while True:
        if head_A is None:
            tail.next = head_B
            break
        if head_B is None:
            tail.next = head_A
            break
        if head_A.data <= head_B.data:
            tail.next = head_A
            head_A = head_A.next
        else:
            tail.next = head_B
            head_B = head_B.next
        tail = tail.next
    return dummyNode.next
#{ 
#  Driver Code Starts
#Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()
if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        for x in nodes_b:
            b.append(x)
        printList(sortedMerge(a.head,b.head))
# } Driver Code Ends
"""
