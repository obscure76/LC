class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = len(A) - 1
        while i > 0:
            if A[i] < A[i - 1]:
                break
            i -= 1
        if i == 0:
            return A
        j = len(A) - 1
        while j >= i:
            if A[j] < A[i - 1]:
                while A[j] == A[j - 1]:
                    j -= 1
                break
            j -= 1
        A[i - 1], A[j] = A[j], A[i - 1]
        return A


A = [1,1,5]
print Solution().prevPermOpt1(A)
