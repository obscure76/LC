import random
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def is_sorted(A):
            n = len(A)
            for i in xrange(1, n):
                if A[i] < A[i-1]:
                    return False
            return True
        res = []

        def soort(A, l, r):
            for i in xrange(l, (l+r)/2):
                A[i], A[r-i] = A[r-i], A[i]
        while True:
            if is_sorted(A):
                return res
            x = random.randint(1, len(A))
            soort(A, 1, x)


s = Solution()
A = [3,2,4,1]
s.pancakeSort(A)
