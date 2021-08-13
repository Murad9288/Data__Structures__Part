

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


# A function to do inorder tree traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above function
if __name__=="__main__":

    root = Node(50)
    '''
                ___ 50 ___
    '''
    root = insert(root, 30)
    '''
                ___ 50 ___
             / 
            30
    '''
    root = insert(root, 20)
    '''
                ___ 50 ___
             /
           _30_
         /
        20
    '''
    root = insert(root, 40)
    '''
                ___ 50 ___
             /
           _30_
         /      \
        20      40
    '''
    root = insert(root, 70)
    '''
                ___ 50 ___
             /              \
           _30_             70
         /      \
        20      40
    '''
    root = insert(root, 60)
    '''
                ___ 50 ___
             /              \
           _30_           _ 70_
         /      \       /    
        20      40     60
    '''
    root = insert(root, 80)
    '''
                ___ 50 ___
             /              \
           _30_           _ 70_
         /      \       /       \
        20      40     60       80 
    '''
    
    print("Binary search tree inorder traversal")
    inorder(root)
