#problem name: HORRIBLE - Horrible Queries
# online judge: spoj

arr = [0]*100000*3
lazy = [0]*100000*3

def query(node,l,r,a,b):
    if l>b or r<a:
        return 0
    ret =(min(b,r)-max(a,l)+1)*arr[node]
    if a<=l and r<=b:
        ret += lazy[node]
    else:
        mi = (l+r)//2
        ret += query(2*node+1,l,mi,a,b)+query(2*node+2,mi+1,r,a,b)
    return ret

def update(node,l,r,a,b,x):
    if l>b or r<a:
        return
    if a<=l and r<=b:
        arr[node] += x
    else:
        mi = (l+r)//2
        left = node*2+1
        right = node*2+2
        update(left,l,mi,a,b,x)
        update(right,mi+1,r,a,b,x)
        lazy[node] = lazy[left]+lazy[right]+(mi-l+1)*arr[left]+(r-mi)*arr[right]

if __name__ == '__main__':
    for _ in range(int(input())):
        n,c = map(int,input().split())
        for _ in range(c):
            ab = list(map(int,input().split()))
            o = ab[0]
            p = ab[1]
            q = ab[2]
            if o == 0:
                v = ab[3]
                update(0, 1, n, p, q, v)
            else:
                print(query(0, 1, n, p, q))







