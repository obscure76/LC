import random
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        [3,2,4,1]
        [4,2,4,3]
        """

        def is_sorted(A):
            n = len(A)
            for i in xrange(1, n):
                if A[i] < A[i - 1]:
                    return False
            return True

        def flip(A, idx):
            l, r = 0, idx
            while l <= r:
                A[l], A[r] = A[r], A[l]
                l, r = l + 1, r - 1

        res = []
        n = len(A)

        def pan_sort(A):
            if is_sorted(A):
                return True
            print A,res
            i = random.randint(2, len(A)-1)
            res.append(i)
            flip(A, i)
            if pan_sort(A):
                return True
            flip(A, i)
            res.pop(-1)
        pan_sort(A)
        return res
A = [3,2,4,1]
s = Solution().pancakeSort(A)
