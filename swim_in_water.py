import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        b = grid[0][0]
        m, n = len(grid), len(grid[0])
        #print m,n
        g = grid
        s = [(g[0][0], 0, 0)]
        visit = {(0,0):1}
        while s:
            v, i, j = heapq.heappop(s)
            #print i,j, v,
            b = max(b, v)
            if i==m-1 and j==n-1:
                return b
            if i+1<m and (i+1,j) not in visit:
                visit[(i+1, j)] = 1
                heapq.heappush(s, (g[i+1][j], i+1, j))
            if j+1<n and (i,j+1) not in visit:
                heapq.heappush(s, (g[i][j+1], i, j+1))
                visit[(i,j+1)] = 1
            if i > 0 and (i-1,j) not in visit:
                visit[(i-1,j)] = 1
                heapq.heappush(s, (g[i-1][j],i-1,j))
            if j>0 and (i, j-1) not in visit:
                visit[(i,j-1)] = 1
                heapq.heappush(s, (g[i][j-1], i, j-1))
            #print s

        return b


inp = [[0,2],[1,3]]
print Solution().swimInWater(inp)
inp = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print Solution().swimInWater(inp)