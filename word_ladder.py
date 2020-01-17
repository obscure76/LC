class Solution(object):
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        q = {beginWord:1}
        nq = {}
        v = {}
        p = {beginWord: {}}
        d = {}
        for w in wordList:
            d[w] = 1
        res = []
        pre = []

        def path(n, pre):
            if n == beginWord:
                res.append(pre[:][::-1])
                return
            for k in p[n]:
                if k in pre:
                    continue
                pre.append(k)
                path(k, pre)
                pre.pop(-1)

        def neighbor(w):
            for i in xrange(len(w)):
                for c in Solution.ALPHA:
                    yield w[:i] + c + w[i+1:]

        found = False
        while len(q):
            #print q
            for w in q:
                if w == endWord:
                    found = True
                    continue
                #print w
                for nw in neighbor(w):
                    if nw in d:
                        if nw != w and nw not in v and nw not in q:
                            if nw in p:
                                p[nw][w] = 1
                            else:
                                p[nw] = {w:1}
                            nq[nw] = 1
                v[w] = 1
            if not found:
                q, nq = nq, {}
            else:
                #print q, nq
                break
        #print p
        if endWord in p:
            pre.append(endWord)
            path(endWord, pre)
        return res


print Solution().findLadders('hit', 'cog', ['hot', 'dot', 'lot', 'log', 'cog', 'dog'])