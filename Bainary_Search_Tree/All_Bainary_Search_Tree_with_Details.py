# বাইনারি সার্চ ট্রি-এর ক্ষেত্রে ২ টি বিষয় মাথায় রাখতে হবে:
'''
১. যদি ট্রি-তে আগে থেকে কোনো নোড না থাকে (অর্থাৎ বর্তমান root নোড none থাকবে),
            তাহলে নতুন যোগ করা নোডটিই হবে ট্রি- এর root নোড । আবার-
২. নতুন নোডটি যদি root নোডের সরাসরি চাইল্ড হয়, তাহলেও root  নোডের  পরিবর্তন ঘটবে।
            এ কারণেই আমরা root নোডকে রিটার্ন করি।
'''
# There are two things to keep in mind when it comes to binary search trees:
'''
1. If the tree does not already have a node (ie the existing root node will have none), 
                then the newly added node will be the root node of the tree. Again
2. If the new node is a direct child of the root node, the root node will also change. 
                This is why we return to the root node.
'''
# 1st system:

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        node.parent = self

# now bst_insert:
def bst_insert(root,node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
    if last_node is None:
        # tree was empty. node is the only node, hence root
        root = node # new node add
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root
'''
              _10_
             /    \
            5      17
           /      /  \
          3      12  19
         / \             
        1   4         
   
'''
# now create_bst:
def create_bst():
    li = list(map(int,input().split()))
    root = TreeNode(li)
    for item in root:
        node = TreeNode(item)
        root = bst_insert(root, node)
    return root

# In_order tree traverse:
def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

# bst- tree minimum node:
def bst_minimum(root):
    while root.left is not None:
        root = root.left
    print(root)

# bst_tree maximum node:
def bst_maximum(root):
    while root.right is not None:
        root = root.right
    print(root)


# এখন আমরা BST-তে কোনো ডেটা খুঁজে বের করার ফাংশন টি লিখে ফেলি।
# Now we write the function to find any data in BST.
def best_search(node,key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right
    return node

# Now check to your code:
if __name__ == "__main__":
    root = create_bst()
    print("Tree is root =",root)
    print()
    # In_order tree traverse:
    print("In_order Tree:")
    in_order(root)
    print()

    # bst- tree minimum node:
    print("Minimum node:")
    bst_minimum(root)
    print()

    # bst_tree maximum node:
    print("Maximum node:")
    bst_maximum(root)
    print()

    # input with searching:
    print("bst_search:")
    for key in [int(input("Please Enter the search key: ")),int(input("Please Enter the search key: "))]:
        print("Searching =",key)
        result = best_search(root, key)
        print("Result =",result)


# second system:
"""
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        node.parent = self

# now bst_insert:
def bst_insert(root,node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
    if last_node is None:
        # tree was empty. node is the only node, hence root
        root = node # new node add
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root
'''
              _10_
             /    \
            5      17
           /      /  \
          3      12  19
         / \             
        1   4         
   
'''
# now create_bst:
def create_bst():
    root = TreeNode(10)
    for item in [5,17,3,7,12,19,1,4]:
        node = TreeNode(item)
        root = bst_insert(root, node)
    return root

# In_order tree traverse:
def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

# bst- tree minimum node:
def bst_minimum(root):
    while root.left is not None:
        root = root.left
    print(root)

# Node transfer:
def bst_transfer(root, current_node, new_node):
    if current_node.parent is None:
        root = new_node
    elif current_node == current_node.parent.left:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)
    return root

# Node delete:
def bst_delete(root,node):
    if node.left is None:
        root = bst_transfer(root,node,node.right)
    elif node.right is None:
        root = bst_transfer(root,node,node.left)

    else:
        min_node = bst_minimum(node.right)
        if min_node.parent != node:
            root = bst_transfer(root,min_node,min_node.right)
            min_node.add_right(node.right)
        root = bst_transfer(root,node,min_node)
        min_node.add_left(node.left)
    return root



# এখন আমরা BST-তে কোনো ডেটা খুঁজে বের করার ফাংশন টি লিখে ফেলি।
# Now we write the function to find any data in BST.
def best_search(node,key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right
    return node

# Now check to your code:
if __name__ == "__main__":
    root = create_bst()
    print("Tree is root =",root)
    print()

    print("BST:")
    in_order(root)

    for key in [1,5,10]:
        node = best_search(root,key)
        print("will delete =", node)
        root = bst_delete(root,node)
        print("BST:")
        in_order(root)
"""
