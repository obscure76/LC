import collections


class Solution(object):

    def wordSubsets(self, A, B):
        BC = [collections.Counter(b) for b in B]
        r = []
        for a in A:
            ac = collections.Counter(a)
            notFound = False
            for bc in BC:
                for k in bc:
                    if ac[k] < bc[k]:
                        notFound = True
                        break
                if notFound:
                    break
            if not notFound:
                r.append(a)
        return r


s = Solution()
A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]
print s.wordSubsets(A, B)
A = ["amazon","apple","facebook","google","leetcode"]
B = ["l","e"]
print s.wordSubsets(A, B)
A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]
print s.wordSubsets(A, B)