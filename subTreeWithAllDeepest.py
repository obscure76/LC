# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print_node(self):
        print (self.val,)
        if self.left:
            self.left.print_node()
        if self.right:
            self.right.print_node()


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        d = depth(root)-1

        def lca(node, l):
            if not node or l == d:
                return node
            left = lca(node.left, l + 1)
            right = lca(node.right, l + 1)
            if left and right:
                return node
            elif left:
                return left
            else:
                return right

        return lca(root, 0)

'''
[3,5,1,6,2,0,8,null,null,7,4]
'''
r = TreeNode(3)
r.left = TreeNode(5)
r.left.left = TreeNode(6)
r.left.right = TreeNode(2)
r.left.right.left = TreeNode(7)
r.left.right.right = TreeNode(4)
r.right = TreeNode(1)
r.right.left = TreeNode(0)
r.right.right = TreeNode(8)
res = Solution().subtreeWithAllDeepest(r)
res.print_node()
