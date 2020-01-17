class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        t = sum(x for x in A if x % 2 == 0)
        r = []
        for v, i in queries:
            p = A[i]
            A[i] = A[i] + v
            if A[i] % 2:
                if p % 2 == 0:
                    t -= p
            else:
                if p % 2:
                    t += A[i]
                else:
                    t += v
            r.append(t)
        return r

A = [1,2,3,4]
q = [[1,0],[-3,1],[-4,0],[2,3]]
exp = [8,6,2,4]
print "sol", Solution().sumEvenAfterQueries(A, q)
print "exp", exp