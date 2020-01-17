class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        allLists = [[] for _ in range(min(numRows, len(s)))]
        print allLists
        i = 0
        down = True
        for c in s:
            allLists[i].append(c)
            i += 1 if down else -1
            if i == numRows or i == -1:
                down = not down
                i += 1 if down else -1
        print allLists
        return "".join("".join(x) for x in allLists)


S = Solution()
print S.convert("PAYPALISHIRING", 3)

