# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        def build(pre, prel, prer, post, pol, por):
            if prel >= prer:
                return None
            node = TreeNode(pre[prel])
            print node.val
            if prer - prel == 1:
                return node
            L = get_index(post, pol, por, pre[prel + 1]) - pol + 1
            node.left = build(pre, prel + 1, prel + 1 + L, post, pol, pol+L)
            node.right = build(pre, prel + 1 +L, prer, post, pol + L, por)
            return node

        def get_index(post, l, r, v):
            for i in xrange(l, r+1):
                if post[i] == v:
                    return i
        return build(pre, 0, len(pre), post, 0, len(post))

    def contruct(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.contruct(pre[1:L+1], post[:L])
        root.right = self.contruct(pre[L+1:], post[L:-1])
        return root


pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

t = Solution().constructFromPrePost(pre, post)


def traverse(n):
    if n:
        traverse(n.left)
        print n.val,
        traverse(n.right)
traverse(t)

t = Solution().constructFromPrePost([2,1], [1,2])
traverse(t)