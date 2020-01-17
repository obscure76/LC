import copy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            n = len(res)
            for j in xrange(n):
                res.append(copy.deepcopy(res[j]))
                res[-1].append(i)
        return res

    def subsets_v2(self, nums):
        n = len(nums)
        res = []
        for i in xrange(2**n):
            t = []
            for j in xrange(n):
                if 1<<j & i:
                    t.append(nums[j])
            res.append(t)
        return res


nums = [1,2,3]
print Solution().subsets(nums)

print Solution().subsets_v2(nums)
