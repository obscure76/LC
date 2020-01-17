class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution(object):
    pi = 0

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = [x for x in preorder]
        inorder.sort()
        n = len(preorder)
        return self.construct(inorder, 0, n - 1, preorder)

    def construct(self, inorder, il, ir, preorder):
        if il>ir:
            return None
        curr = TreeNode(preorder[self.pi])
        self.pi += 1
        index = self.index_of(inorder, il, ir, curr.val)
        curr.left = self.construct(inorder, il, index - 1, preorder)
        curr.right = self.construct(inorder, index + 1, ir, preorder)
        return curr

    def index_of(self, inorder, l, r, val):
        for i in range(l, r+1):
            if inorder[i] == val:
                return i
        return -1

    def traverse(self, node, res):
        if not node:
            return

        self.traverse(node.left, res)
        res.append(node.val)
        self.traverse(node.right, res)


preorder = [8,5,1,7,10,12]
output = [8,5,10,1,7,None,12]
sol = Solution()
root = sol.bstFromPreorder(preorder)
res = []
sol.traverse(root, res)
print "res", res
print "expected", output
