'''
        insert() function time complexity   : O(n)
        search() function time complexity   : O(n)
'''

# Python Program to insert operation in binary search tree
class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# A function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)

    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root


# A function to search a given key in BST
def search(root, item):
    if root is None or root.val == item:
        return root

    # Key is greater than root's item
    if root.val < item:
        return search(root.right, item)

    # Key is smaller than root's item
    return search(root.left, item)


# A function to do inorder tree traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above function
if __name__=="__main__":

    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Binary search tree inorder traversal")
    inorder(root)


    # search
    print()
    if search(root, 100):
        print('Yes')
    else:
        print('No')
