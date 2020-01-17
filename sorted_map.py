import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = collections.Counter(nums)
        res = sorted(m.items(), key=lambda x: -x[1])
        return [x[1] for x in res[:k]]

    def topk_freq(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = collections.Counter(nums)
        h = []
        for i, j in m.items():
            heapq.heappush(h, (-j, i))
            if len(h) > k:
                heapq.heappop(h)
        return h
        print h


Solution().topKFrequent([1,1,1,2], 2)
Solution().topk_freq([1,1,1,2], 2)

