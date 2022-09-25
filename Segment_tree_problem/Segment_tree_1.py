

#
#
# Data-structure -> Segment-Tree
# Time:- O(n log n)
#
#



arr = [4, -9, 3, 7, 1, 0, 2]
n = len(arr)
tree = [0]*(n*3)

def init(node, b, e):

    if b == e:
        tree[node] = arr[b]
        return

    Left = node * 2
    Right = node * 2 + 1
    mid = (b + e) // 2
    init(Left, b, mid)
    init(Right, mid + 1, e)
    tree[node] = tree[Left] + tree[Right]

def query(node, b, e, i, j):

    if i > e or j < b:
        return 0
    if b >= i and e <= j:
        return tree[node]

    Left = node * 2
    Right = node * 2 + 1
    mid = (b + e) // 2
    p1 = query(Left, b, mid, i, j)
    p2 = query(Right, mid+1, e, i, j)
    return p1 + p2

def update(node, b, e, i, newvalue):

    if i > e or i < b:
        return
    if b >= i and e <= i:
        tree[node] = newvalue
        return

    Left = node * 2
    Right = node * 2+1
    mid = (b + e) // 2
    update(Left, b, mid, i, newvalue)
    update(Right, mid+1, e, i, newvalue)
    tree[node] = tree[Left] + tree[Right]


if __name__== "__main__":
    init(1, 0, n-1)
    print("Array is: ", arr)
    print("Initialize Tree: ", tree)
    i, j = 2, 5
    res = query(1, 1, n-1, i, j)
    print("Sum is index i to j:", res)
    update(1, 0, n-1, 4, 5)
    print("Updated Tree:", tree)
    res = query(0, 0, n-1, i, j)
    print("Sum is index i to j:", res)
