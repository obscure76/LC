import collections


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        m = collections.defaultdict(int)
        for e in emails:
            n = len(e)
            l = []
            d = []
            t = ''
            for i in xrange(n - 1, -1, -1):
                if e[i] == '.' and not l:
                    l = t
                    t = ''
                elif e[i] == '@':
                    d = t
                    t = ''
                elif e[i] == '+':
                    t = ''
                elif e[i] == '.' and d:
                    pass
                else:
                    t += e[i]
            #print e, r
            m[t+d+l] += 1
        return len(m)


inp = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print Solution().numUniqueEmails(inp)
