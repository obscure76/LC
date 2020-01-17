class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nextn = None
        self.prev = None

    def add_to_front(self, node):
        nextn = self.nextn
        self.nextn = node
        node.prev = self
        nextn.prev = node
        node.nextn = nextn

    def move_to_front(self, node):
        prev = node.prev
        prev.nextn = node.nextn
        node.nextn.prev = prev
        self.add_to_front(node)

    def remove(self):
        tail = self.prev
        tail.prev.nextn = self
        self.prev = tail.prev
        return tail.key


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.m = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.nextn = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.m:
            return -1
        node = self.m[key]
        self.head.move_to_front(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.m:
            return
        node = ListNode(key, value)
        self.m[key] = node
        self.head.add_to_front(node)
        if len(self.m) > self.cap:
            k = self.tail.remove()
            self.m.pop(k)

    def print_list(self):
        n = self.head
        while n:
            print n.val,
            n = n.nextn


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# inp1 = ["LRUCache","put","put","get","put","get","put","get","get","get"]
# inp2 = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
# output = [1,-1,-1,3,4]
inp1 = ["LRUCache","put","put","get","put","put","get"]
inp2 = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
output = [1, -1, 2]

j = 0
cache = None
gets = []
for i in xrange(0, len(inp1)):
    print inp1[i],inp2[i],
    if inp1[i] == "LRUCache":
        cache = LRUCache(inp2[j][0])
        j += 1
        print ""
    elif inp1[i] == "put":
        cache.put(inp2[j][0], inp2[j][1])
        print cache.print_list()
        print ""
        j += 1
    else:
        gets.append(cache.get(inp2[j][0]))
        cache.print_list()
        print ""
        j += 1
print gets
print output


