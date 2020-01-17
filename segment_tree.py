import math


def build_seg_tree(tree, arr, ti, l, r):
    if l == r:
        tree[ti] = arr[l]
        return
    m = (l+r)/2
    build_seg_tree(tree, arr, 2*ti+1, l, m)
    build_seg_tree(tree, arr, 2*ti+2, m+1, r)
    tree[ti] = merge(tree[2*ti+1], tree[2*ti+2])


def build_seg_tree_v2(nums):
    n = len(nums)
    print n
    my_tree = [0]*(2*n)
    for i in xrange(n, 2*n):
        my_tree[i] = nums[i-n]
    for i in xrange(n-1, 0, -1):
        my_tree[i] = my_tree[i*2] + my_tree[i*2+1]
    return my_tree


def merge(a, b):
    return a+b


def query_seg_tree(tree, ti, l, r, i, j):
    if l>j or r<i:
        return 0
    if i<=l or j>=r:
        return tree[ti]
    m = (l+r)/2
    if i>m:
        return query_seg_tree(tree, 2*ti+2, m+1, r, i, j)
    elif j<=m:
        return query_seg_tree(tree, 2*ti+1, l, m, i, j)
    return query_seg_tree(tree, 2*ti+1, l, m, i, m) + query_seg_tree(tree, 2*ti+2, m, r, m+1, j)


def update_tree(tree, nums, i, nval):
    def update(ss, se, i, diff, si):
        if i<ss or i>se:
            return
        tree[si] = tree[si] + diff
        if se != ss:
            m = (se+ss)/2
            update(ss, m, i, diff, 2*si+1)
            update(m+1, se, i, diff, 2*si+2)
    n = len(nums)
    if i<0 or i>=n:
        return
    diff = nval - nums[i]
    nums[i] = nval
    update(0, n-1, i, diff, 0)



arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
ll = len(arr)
h = int(math.ceil(math.log(ll, 2)))
# print ll, h
tree = [0]*((2**(h+1))-1)
#tmp = [183, 82, 101, 48, 34, 43, 58, 35, 13, 19, 15, 31, 12, 33, 25, 18, 17, 0, 0, 0, 0, 0, 0, 11, 20, 0, 0, 0, 0, 0, 0]
#print len(tmp)
# print len(tree)
# build_seg_tree(tree, arr, 0, 0, ll-1)
# print tree
#print query_seg_tree(tree, 0, 0, len(tree)-1, 0, 0)
print build_seg_tree_v2(arr)
