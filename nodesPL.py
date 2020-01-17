'''
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

Input: [ [0,0,0,0],
         [1,0,1,0],
         [0,1,1,0],
         [0,0,0,0]  ]
Output: 3
Explanation:
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
'''


class Solution():
    def num_of_land_squares(self, matrix):
        m = matrix
        r , c = len(m), len(m[0])
        rb = [0, len(m)-1]
        q = []
        for i in rb:
            for j in xrange(c):
                if m[i][j]:
                    m[i][j] = 'B'
                    q.append((i,j))
        cb = [0, len(m[0])-1]
        for j in cb:
            for i in xrange(r):
                if m[i][j]:
                    m[i][j] = 'B'
                    q.append((i, j))
        while q:
            x, y = q.pop(0)
            if x-1 > 0 and m[x-1][y] == 1:
                q.append((x-1, y))
                m[x-1][y] = 'B'
            if x+1 < r and m[x+1][y] == 1:
                q.append((x + 1, y))
                m[x + 1][y] = 'B'
            if y-1 > 0 and m[x][y-1] == 1:
                m[x][y-1] = 'B'
                q.append((x, y-1))
            if y+1 < c and m[x][y+1] == 1:
                m[x][y+1] = 'B'
                q.append((x, y+1))
        res = 0
        for i in xrange(r):
            for j in xrange(c):
                if m[i][j] == 1:
                    res += 1
        return res

inp = [[0,0,0,0],
       [1,0,1,0],
         [0,1,1,0],
         [0,0,0,0]]

print Solution().num_of_land_squares(inp)

inp = [[0,1,1,0],
       [0,0,1,0],
       [0,0,1,0],
       [0,0,0,0]]

print Solution().num_of_land_squares(inp)
for r in inp:
    print r