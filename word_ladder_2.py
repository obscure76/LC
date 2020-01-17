class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def neigh(w):
            for i in xrange(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    yield w[:i]+c+w[i+1:]
        b, e = beginWord, endWord
        wl = {w:1 for w in wordList}
        q = {b:1}
        nq = {}
        i = 0
        l = 1
        while q:
            w = q.popitem()[0]

            if w == e:
                return l
            for nw in neigh(w):
                if nw in wl:
                    nq[nw] = 1
                    wl.pop(nw)
            if not q:
                q = nq
                nq = {}
                l += 1
        return 0

    def ladderLengthV2(self, beginWord, endWord, wordList):
        def neigh(w):
            for i in xrange(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    yield w[:i]+c+w[i+1:]

        b, e = beginWord, endWord
        wl = {w: 1 for w in wordList}
        q = set()
        q.add(b)
        nq = set()
        l = 1
        while q:
            w = q.pop()
            if w == e:
                return l
            for nw in neigh(w):
                if nw in wl:
                    nq.add(nw)
                    wl.pop(nw)
            if not q:
                q, nq, l = nq, set(), l+1
        return 0

b = "hit"
e = "cog"
wl = ["hot","dot","dog","lot","log","cog"]
print Solution().ladderLengthV2(b,e,wl)
