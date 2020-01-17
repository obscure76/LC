from heapq import heappop, heappush

class Graph(object):
    def __init__(self):
        pass

    def build_graph(self, edges):
        g = {}
        for s, d in edges:
            if s in g:
                g[s][d] = 1
            else:
                g[s] = {d:1}
        return g

    def build_graph_bidir(self, edges):
        g = {}

        for s,d in edges:
            if s in g:
                g[s][d] = 1
            else:
                g[s] = {d:1}
            if d in g:
                g[d][s] = 1
            else:
                g[d] = {s: 1}
        return g

    def build_graph_weights(self, edges):
        g = {}

        for s,d,w in edges:
            if s in g:
                g[s][d] = w
            else:
                g[s] = {d:w}
        return g

    def bfs(self, g, s):
        q = [s]
        v = {}
        while q:
            n = q.pop(0)
            v[n] = 1
            for nb in g.get(n, {}):
                if nb not in v:
                    q.append(nb)

    def dfs(self, g, s):
        def dfss(s):
            for nb in g.get(s, {}):
                dfss(nb)
        dfss(s)

    def dijkstra(self, g, s):
        d = [(0,s)]
        m = 1000000
        while d:
            w, u = heappop(d)
            for nb in g.get(u, {}):
                heappush(d, (w+g[u][nb], nb))
                if m>w+g[u][nb]:
                    m = w+g[u][nb]



    def has_cycle(self, g):
        pass

    def bellman_ford(self, edges, N, K):
        d = {}
        for i in xrange(1, N + 1):
            d[i] = 1000000
        d[K] = 0
        m = 0
        for i in xrange(1, N + 1):
            for u, v, w in edges:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
        for i in xrange(1, N + 1):
            if d[i] == 1000000:
                return -1
        return max(d.values())

    def floyd_warshall(self, edges, N, K):
        d = {i:{j:1000000 for j in xrange(1, N+1)} for i in xrange(1, N+1)}
        for i in xrange(1, N+1):
            d[i][i] = 0
        for u,v,w in edges:
            d[u][v] = w
        for i in xrange(1, N+1):
            for j in xrange(1, N+1):
                for k in xrange(1, N+1):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][k] = d[i][k] + d[k][j]





