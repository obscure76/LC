class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def partition(nums, begin, end):
            pivot = begin
            for i in range(begin+1, end+1):
                if nums[i] <= nums[begin]:
                    pivot += 1
                    nums[i], nums[pivot] = nums[pivot], nums[i]
            nums[pivot], nums[begin] = nums[begin], nums[pivot]
            return pivot

        def quickSort(nums, begin=0, end=len(nums)-1):
            if begin >= end:
                return
            p = partition(nums, begin, end)
            quickSort(nums, begin, p-1)
            quickSort(nums, p+1, end)

        quickSort(nums)
        return nums


A = [3, 4, 1, 2, 7]
print Solution().sortArray(A)
