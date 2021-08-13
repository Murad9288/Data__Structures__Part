# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Linkedlist Class
class Linkedlist:
	def __init__(self):
		self.head = None


	def push(self, new_data):
		current_node = Node(new_data)
		current_node.next = self.head
		self.head = current_node


	def deletePositionNode(self, position):
		if position == 0:
			self.head = self.head.next

		else:
			node = self.head
			for _ in range(position - 1):
				node = node.next

			node.next = node.next.next

		return self.head



	def printlist(self):
		current_node = self.head
		while current_node:
			print(current_node.data, end=" ")
			current_node = current_node.next



if __name__ == '__main__':

	llist = Linkedlist()
	llist.push(2)
	llist.push(9)
	llist.push(5)
	llist.push(4)
	llist.push(1)

	print("Before linkedlist:->", end=" ")
	llist.printlist()

	llist.deletePositionNode(3)

	print('\nAfter linkedlist:->', end=" ")
	llist.printlist()
