class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        root = []

        class TreeNode(object):
            def __init__(self, val):
                self.val = val
                self.left = self.right = None

        def insert(x, root):
            if not root:
                root.append(TreeNode(x))
                return
            n = root[0]
            p = None
            while n:
                p = n
                if n.val < x:
                    n = n.right
                else:
                    n = n.left
            if p.val < x:
                p.right = TreeNode(x)
            else:
                p.left = TreeNode(x)

        def search(x, root):
            n = root[0]
            while n:
                if n.val <= x:
                    n = n.right
                else:
                    return n.val
            return -1

        def traverse(n):
            if n:
                traverse(n.left)
                print n.val,
                traverse(n.right)

        res = []

        for x in nums2:
            insert(x, root)

        traverse(root[0])

        for x in nums1:
            res.append(search(x, root))

        print res
t = set()

nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution().nextGreaterElement(nums1, nums2)
