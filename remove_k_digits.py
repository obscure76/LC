class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s = []
        d = len(num)-k
        for i in num:
            while s and k and i<s[-1]:
                s.pop()
                k -= 1
            s.append(i)
        return ''.join(s[:-k or None]).lstrip('0') or '0'

num = "1234567890"
k = 9
print Solution().removeKdigits(num, k)