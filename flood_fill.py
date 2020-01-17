class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        q = []
        m, n = len(image), len(image[0])
        t = image[sr][sc]
        if t != newColor:
            q.append((sr, sc))
        while q:
            r, c = q.pop(0)
            image[r][c] = newColor
            if r > 0 and image[r - 1][c] == t:
                q.append((r - 1, c))
            if r < m - 1 and image[r + 1][c] == t:
                q.append((r + 1, c))
            if c > 0 and image[r][c - 1] == t:
                q.append((r, c - 1))
            if c < n - 1 and image[r][c + 1] == t:
                q.append((r, c + 1))
        return image

inp = [[1,1,1],[1,1,0],[1,0,1]]
for x in Solution().floodFill(inp, 1, 1, 2):
    print x
exp = [[2,2,2],[2,2,0],[2,0,1]]
print "output"
for x in exp:
    print x
inp = [[0,0,0],[0,1,1]]
for x in Solution().floodFill(inp, 1, 1, 1):
    print x
