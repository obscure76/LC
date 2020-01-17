# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


import collections


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        t = head
        m = collections.defaultdict(int)
        while t.next:
            m[t.val] = t.next.val
            t = t.next
        r = 0
        i = 0
        s = True
        for i in xrange(1, len(G)):
            if m[G[i - 1]] != G[i]:
                r += 1
                s = True
            else:
                s = False
        if s:
            r += 1
        return r


'''
[0,1,2,3]
[0,1,3]
'''
l = ListNode(0)
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
G = [0,1,3]
print Solution().numComponents(l,G)
