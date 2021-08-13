'''
        inorder()function time complexity   : O(n)
        insert() function time complexity   : O(n)
        delete() function time complexity   : O(n)
'''

# Python program to delete operation
# in binary search tree(BST)

# A Binary Tree Node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# A function to do inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


# A function to insert a new node
def insert(root, key):
    # if the tree is empty, return a new node
    if root is None:
        return Node(key)

    # otherwise recur down the tree
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root


# A function min key value found in that tree
def minValueNode(root):
    while root.left is not None:
        root = root.left

    return root


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
    # Base case
    if root is None:
        return root

    # if the key to be deleted is smaller than the root's
    # key then it lies in left subtree
    if root.val > key:
        root.left = deleteNode(root.left, key)

    # if the key to be delete is greater then the root's key
    # then it lies in right subtree
    elif root.val < key:
        root.right = deleteNode(root.right, key)

    else:

        # Node with only child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children Get teh inorder successor
        # smallest in the right subtree
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root


# Driver program to test above functions
if __name__ == '__main__':
    """ Let us create following BST 
                  50 
               /     \ 
              30      70 
             /  \    /  \ 
           20   40  60   80
                   /   
                  55
    inorder traversal->[20, 30, 40, 50, 55, 60, 70, 80]
    """
    root = None
    root = insert(root, 80)
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 55)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)

    print("Inorder traversal of the given tree")
    inorder(root)

    print("\n\nDelete->50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\n\nDelete->20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\n\nDelete->30")
    root = deleteNode(root, 70)
    print("Inorder traversal of the modified tree")
    inorder(root)
