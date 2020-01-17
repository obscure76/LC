class Node():
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nh = tmp = Node(0, None, None)
        t = head
        while t:
            nh.next = Node(t.val, None, t.random)
            t.random = nh.next
            t = t.next
            nh = nh.next
        nh = tmp.next
        t = head
        while t:
            l = nh.random
            if nh.random:
                nh.random = nh.random.random
            t.random = l
            t = t.next
            nh = nh.next
        return tmp.next


t = h = Node(1, None, None)
h.next = Node(2, None, None)
h.random = h.next
h.next.random = h.next

while t:
    print t, t.val, t.random, t.random.val, '  ',
    t = t.next

print ''

r = Solution().copyRandomList(h)
'''
{"$id":"1",
"next":{"$id":"2","next":{"$id":"3","next":{"$id":"4","next":{"$id":"5","next":null,"random":{"$ref":"1"},"val":4},"random":null,"val":-3},"random":null,"val":7},"random":{"$ref":"4"},"val":8},"random":{"$ref":"5"},"val":-1}
'''
while r:
    print r, r.val, r.random, r.random.val, '  ',
    r = r.next
