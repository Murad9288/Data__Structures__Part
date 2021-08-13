# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        current = Node(new_data)
        current.next = self.head
        self.head = current

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Given Linked List")
    llist.printList()

    llist.reverse()
    print("\nReversed Linked List")
    llist.printList()

    
    
    
    
    
    
    
    
    
    '''
# Reversed Array:
def reverse(array):
    left = 0
    right = len(array)-1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array
array = [1, 2, 3]
res = reverse(array)
print(res)
'''
