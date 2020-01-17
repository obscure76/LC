#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.nextn = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.nextn is None:
            return head
        s, f, p = head, head, None
        while f and f.nextn:
            p = s
            s = s.nextn
            f = f.nextn.nextn
        p.nextn = None
        l1 = self.sortList(head)
        l2 = self.sortList(s)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        t = h = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                t.nextn = l1
                l1 = l1.nextn
            else:
                t.nextn = l2
                l2 = l2.nextn
            t = t.nextn
        if l1:
            t.nextn = l1
        elif l2:
            t.nextn = l2
        return h.nextn
    

h = ListNode(4)
h.nextn = ListNode(3)
h.nextn.nextn = ListNode(1)
h.nextn.nextn.nextn = ListNode(2)
c = h
while c:
    print c.val,
    c = c.nextn
res =  Solution().sortList(h)
print ""
while res:
    print res.val,
    res = res.nextn

