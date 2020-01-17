class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        m, n = len(A), len(B)
        res = []
        while i < m and j < n:
            lmax = max(A[i][0], B[j][0])
            rmin = min(A[i][1], B[j][1])
            if lmax <= rmin:
                res.append([lmax, rmin])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


s = Solution()
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print "Expected [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]"
print "Result", s.intervalIntersection(A, B)
