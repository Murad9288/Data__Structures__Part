# segment tree:
# lightoj: problem name: array queries.

def init_segment_tree(b,e,node):
    if b == e:
        tree[node] = arr[b]
        return arr[b]
    x = init_segment_tree(b,(b+e)//2,node*2)
    y = init_segment_tree(((b+e)//2)+1,e,node*2+1)
    tree[node] = min(x,y)
    return tree[node]

def query(l,r,e,f,node):
    if e <= l and f>= r:
        return tree[node]
    if e>r or f<l:
        return int(1e9)
    x = query(l,(l+r)//2,e,f,node*2)
    y = query(((l+r)//2)+1,r,e,f,node*2+1)
    return min(x,y)

if __name__=="__main__":
    for t in range(int(input())):
        input()
        n,q = map(int,input().split())
        arr = list(map(int,input().split()))
        tree = [0]*n*4
        mx = int(1e9)
        init_segment_tree(0,n-1,0)
        print("Case %d:"%(t+1))
        for d in range(q):
            x,y = map(int,input().split())
            print(query(1,n,x,y,0))