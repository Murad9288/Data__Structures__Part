class Node:
     def __init__(self,data):
          self.data = data
          self.next = None
          self.prev = None

class Doubl_Linked_List:
     def __init__(self):
          self.head = None

     def append(self,data):
          if self.head is None:
               new_node = Node(data)
               new_node.prev = None
               self.head = new_node
          else:
               new_node = Node(data)
               current_node = self.head
               while current_node.next:
                    current_node = current_node.next
               current_node.next = new_node
               new_node.prev = current_node
               new_node.next = None



     def prepend(self,data):
          if self.head is None:
               new_node = Node(data)
               new_node.prev = None
               self.head = new_node
          else:
               new_node = Node(data)
               self.head.prev = new_node
               new_node.next = self.head
               self.head = new_node
               new_node.prev = None

     def print_list(self):
          current_node = self.head
          while current_node:
               print(current_node.data)
               current_node = current_node.next

L = Doubl_Linked_List()
L.prepend(0)
L.append(1)
L.append(4)
L.append(3)
L.prepend(2)

L.print_list()
