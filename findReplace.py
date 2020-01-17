class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        r = []
        for w in words:
            pm = {}
            wm = {}
            try:
                for i, c in enumerate(w):
                    if c not in wm and pattern[i] not in pm:
                        wm[c] = pattern[i]
                        pm[pattern[i]] = c
                    elif wm[c] != pattern[i] or pm[pattern[i]] != c:
                        break
                else:
                    r.append(w)
            except Exception:
                pass
        return r


s = Solution()
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
res = s.findAndReplacePattern(words, pattern)
output = ["mee", "aqq"]
print "words", words
print "res", res
print "out", output
