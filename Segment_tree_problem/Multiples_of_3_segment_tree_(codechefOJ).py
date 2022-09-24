
# Codehef_Problem link: https://www.codechef.com/problems/MULTQ3?tab=statement
# problem name: Multiples of 3


import sys

input = sys.stdin.readline
lazy = [0] * 100005 * 4
arr1 = [0] * 100005 * 4
arr2 = [0] * 100005 * 4
arr3 = [0] * 100005 * 4
try:
    def init_segment_tree(n, b, e):
        if b == e:
            arr1[n] += 1
            arr2[n] = arr3[n] = 0
            lazy[n] = 0
            return
        mid = (b + e) // 2
        left = 2 * n
        right = left + 1
        init_segment_tree(left, b, mid)
        init_segment_tree(right, mid + 1, e)

        arr1[n] = arr1[left] + arr1[right]
        arr2[n] = arr2[left] + arr2[right]
        arr3[n] = arr3[left] + arr3[right]
        lazy[n] = 0


    def push_down(n, b, e):
        left = n * 2
        right = left + 1
        if lazy[n]:
            for i in range(lazy[n]):
                temp = arr1[n]
                arr1[n] = arr3[n]
                arr3[n] = arr2[n]
                arr2[n] = temp
            if b != e:
                lazy[left] += lazy[n]
                lazy[left] %= 3
                lazy[right] += lazy[n]
                lazy[right] %= 3
            lazy[n] = 0


    def update(n, b, e, i, j, new_val):
        push_down(n, b, e)

        if b > j or e < i:
            return
        if b >= i and e <= j:
            lazy[n] += new_val
            lazy[n] %= 3
            push_down(n, b, e)
            return
        mid = (b + e) // 2
        left = 2 * n
        right = left + 1
        update(left, b, mid, i, j, new_val)
        update(right, mid + 1, e, i, j, new_val)
        arr1[n] = arr1[left] + arr1[right]
        arr2[n] = arr2[left] + arr2[right]
        arr3[n] = arr3[left] + arr3[right]


    def query(n, b, e, i, j):
        push_down(n, b, e)
        if b > j or e < i:
            return 0
        if b >= i and e <= j:
            return arr1[n]
        mid = (b + e) // 2
        left = 2 * n
        right = left + 1
        p1 = query(left, b, mid, i, j)
        p2 = query(right, mid + 1, e, i, j)
        return p1 + p2


    if __name__ == "__main__":
        n, q = map(int, input().split())
        init_segment_tree(1, 1, n)
        for _ in range(q):
            ty, l, r = map(int, input().split())
            if ty == 1:
                print(query(1, 1, n, l + 1, r + 1))
            else:
                update(1, 1, n, l + 1, r + 1, 1)
except:
    pass