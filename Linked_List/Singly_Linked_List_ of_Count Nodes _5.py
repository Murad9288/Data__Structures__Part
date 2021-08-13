'''
        # push()              Time complexity   : O(1)
                                      Space complexity  : O(1)

        # getCount()        Time complexity   : O(n)
                                       space complexity  : O(1)
'''


# A complete working python program to find lenght of linkedlist
# Node class

class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linkedlist class Node object
class Linkedlist:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		# Store head node
		current_node = Node(new_data)
		current_node.next = self.head
		self.head = current_node

	# This function is Linkedlist count node
	def getCount(self):
		current_node = self.head
		count = 0

		while current_node:
			current_node = current_node.next
			count += 1

		return count

# Code execution starts here
if __name__ == '__main__':
	llist = Linkedlist()
	llist.push(4)
	llist.push(3)
	llist.push(1)

	# call getCount function
	print("Count of nodes is : ", llist.getCount())
