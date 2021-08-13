# Traversal Tree:
# এইখানে Traversal Tree টা Recursion দিয়ে করানো হয়েছে ।
# Traversal tree - 3 প্রকার:
'''
-যেমনঃ--
১. Pre-order traversal
২. In-order traversal
৩. Post-order traversal
'''
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
           _(2)_
         /          \
     (7)         (9)
     /  \             \
   (1) (6)        (8)
         /   \       /   \
      (5) (10) (3) (4)
'''
def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    three = Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)

    # now return the root node
    return two

# Pre-order(রুবাডা)  [ এইখানে ‍আমি বুঝার জন্য কিছু বাংলা কথা ‍আমার ভাষায় লিখেছি ।]
# রুবাডা অর্থ:
'''
রু = রুট(root)
বা = বাম(left)
ডা = ডান(right)
'''
def pre_order(node):
    print(node) # node holo = root(রুট)
    if node.left:
        # 1st shortota holo = left(বাম)
        pre_order(node.left)
    if node.right:
        # 2nd shortota holo = right(ডান)
        pre_order(node.right)

# In-order(বারুডা)
# বারুডা অর্থ:
'''
বা = বাম(left)
রু = রুট(root)
ডা = ডান(right)
'''
def in_order(node):
    if node.left:
        # 1st shortota holo = left(বাম)
        in_order(node.left)
    print(node)# node holo = root(রুট)
    if node.right:
        # 2nd shortota holo = right(ডান)
        in_order(node.right)

# Post-order(বাডারু)
# বাডারু অর্থ:
'''
বা = বাম(left)
ডা = ডান(right)
রু = রুট(root)
'''
def post_order(node):
    if node.left:
        # 1st shortota holo = left(বাম)
        post_order(node.left)
    if node.right:
        # 2nd shortota holo = right(ডান)
        post_order(node.right)
    print(node) # node holo = root(রুট)

if __name__ == "__main__":
    root = create_tree()
    print("\nPre-order traversal:")
    pre_order(root)
    print("\nIn-order traversal:")
    in_order(root)
    print("\nPost-order traversal:")
    post_order(root)

    
