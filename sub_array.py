class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def sub_sum(n, r):
            t = A[:n]
            c = min(t)
            r[0] += c
            for i in xrange(n, len(A)):
                t.pop(0)
                t.append(A[i])
                r[0] += min(t)
        res = [0]
        for i in xrange(1, len(A)+1):
            sub_sum(i, res)
        return res[0]


inp = [3,1,2,4]
print Solution().sumSubarrayMins(inp)
