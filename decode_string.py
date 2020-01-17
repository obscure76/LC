class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cw = ''
        cn = ''
        for c in S:
            if '0' <= c <= '9':
                cn += c
            else:
                if cn:
                    n = len(cw) * int(cn)
                    if K > n:
                        K -= n
                    else:
                        ind = K % (len(cw))
                        return cw[ind - 1]
                    cn = ''
                    cw = ''
                cw += c
        if not cn:
            cn = '1'
        if cn:
            n = len(cw) * int(cn)
            if K > n:
                K -= n
            else:
                ind = K % (len(cw))
                return cw[ind - 1]


s = Solution()
# inp = "leet2code3"
# K = 10
# print s.decodeAtIndex(inp, K)
# inp = 'Ha22'
# K = 5
# print s.decodeAtIndex(inp, K)
inp = "a2b3c4d5e6f7g8h9"
K = 9
print s.decodeAtIndex(inp, K)
