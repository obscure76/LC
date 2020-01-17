import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dest, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        g = {}
        for u, v, w in flights:
            if u in g:
                g[u][v] = w
            else:
                g[u] = {v: w}
        d = {src: 0}
        q = [(0, 0, src)]
        while q:
            lvl, dst, c = heapq.heappop(q)
            if lvl > K:
                continue
            for nb in g.get(c, {}):
                if nb not in d or d[nb] > dst + g[c][nb]:
                    d[nb] = dst + g[c][nb]
                heapq.heappush(q, (lvl + 1, d[nb], nb))
        print d
        return d[dest] if dest in d else -1


nodes = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
source = 0
dest = 2
K = 1
print Solution().findCheapestPrice(nodes,edges,source,dest,K)
