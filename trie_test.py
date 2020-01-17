class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False


class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def build_trie(self, list_str):
        root = self.root
        for s in list_str:
            self.insert(s, root)
        return root

    def insert(self, s, root):
        p = root
        for c in s:
            if c not in p.children:
                p.children[c] = Node(c)
            p = p.children[c]
        p.end = True

    def search(self, w):
        p = self.root
        for c in w:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.end
