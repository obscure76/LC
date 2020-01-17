# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printx(self):
        print self.val,
        if self.left:
            self.left.printx()
        if self.right:
            self.right.printx()


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        r = [0]
        p = []

        def path(n):
            if not n:
                return
            p.append(n.val)
            if not n.left and not n.right:
                r[0] += val()
                p.pop(-1)
                return
            path(n.left)
            path(n.right)
            p.pop(-1)

        def val():
            print p
            s = 0
            v = 1
            for i in p[::-1]:
                if i:
                    s += v
                v *= 2
            return s
        path(root)

        return r[0]


s = Solution()
r = TreeNode(0)
r.left = TreeNode(1)
r.right = TreeNode(1)
r.printx()
print ""
print s.sumRootToLeaf(r)