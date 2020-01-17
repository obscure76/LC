class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        w = [0]*(n)
        wo = [0]*(n)
        for i in xrange(n-1, -1, -1):
            try:
                w[i] = nums[i]
                val = 0
                if i+2<n:
                    val = max(w[i+2], 0)
                if i+1<n:
                    val = max(wo[i+1], 0)
                w[i] = val + w[i]
                val = 0
                if i+1<n:
                    wo[i] = max(wo[i+1], w[i+1])
            except Exception:
                print i,i+2,i+1
                raise
        return max(w[0], wo[0])


nums = [1,2,3,1]
print Solution().rob(nums)
