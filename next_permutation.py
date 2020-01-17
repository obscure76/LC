class Solution(object):
    def next_permutation(self, nums):
        def reverse(l):
            r = len(nums)-1
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l , r = l+1, r-1
        i = len(nums)-1
        while i >0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            reverse(0)
            return
        i -= 1
        j = len(nums)-1
        while j>i:
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        reverse(i+1)

    def generate_permutations(self, nums):
        def reverse(l):
            r = len(nums)-1
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        while True:
            yield nums
            i = len(nums) - 1
            while i > 0 and nums[i] <= nums[i-1]:
                i -= 1
            if i == 0:
                return
            i -= 1
            j = len(nums)-1
            while j>i:
                if nums[j] > nums[i]:
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            reverse(i+1)

    def permutations(self, nums):
        n = len(nums)
        def perm(l):
            if l == n:
                yield nums
            else:
                for i in xrange(l, n):
                    nums[i], nums[l] = nums[l], nums[i]
                    for x in perm(l+1):
                        yield x
                    nums[i], nums[l] = nums[l], nums[i]
        for x in perm(0):
            yield x


# nums = [1, 2, 3]
# Solution().next_permutation(nums)
# print nums
# print ""
#
# nums = [1,2,3]
# for x in Solution().generate_permutations(nums):
#     print x

nums = [1,2,3]
for x in Solution().permutations(nums):
    print x
