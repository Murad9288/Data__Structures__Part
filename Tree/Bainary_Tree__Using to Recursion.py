class Node:
     def __init__(self,root):
          self.root = root
          self.left = None
          self.right = None

     def __repr__(self):
          return repr(self.root)

     def add_left(self,node):
          self.left = node

     def add_right(self,node):
          self.right = node
'''
Example:
          _2_
        /       \
       7         9
      / \         \
     1   6         8
         / \       / \
       5   10   3   4
'''
def create_tree():
     one = Node(1)
     two = Node(2)
     three = Node(3)
     four = Node(4)
     five = Node(5)
     six = Node(6)
     seven = Node(7)
     eight = Node(8)
     nine = Node(9)
     ten = Node(10)
     two.add_left(seven)
     two.add_right(nine)
     seven.add_left(one)
     seven.add_right(six)
     six.add_left(five)
     six.add_right(ten)
     nine.add_right(eight)
     eight.add_left(three)
     eight.add_right(four)
     print("Root =",two)
     print("Root left =",seven)
     print("Seven left =",one)
     print("Seven right =",six)
     print("Six left =",five)
     print("Six right =",ten)
     print("Root right =",nine)
     print("Nine right =",eight)
     print("Eight left =",three)
     print("Eight right =",four)

if __name__ == "__main__":
    create_tree()
