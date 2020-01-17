"""
# Definition for a Node.

"""

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        def flat(n):
            h = t = n
            if not n:
                return h, h
            while t.next:
                if t.child:
                    on = t.next
                    ch, ct = flat(t.child)
                    t.child = None
                    t.next = ch
                    ch.prev = t
                    ct.next = on
                    t = ct
                    if on:
                        on.prev = ct
                t = t.next
            return h, t

        h, t = flat(head)
        return h




