class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_valid(st, i):
            if i == len(s):
                return True
            for i in xrange(i, len(s)):
                if s[i] == '(':
                    st.append('(')
                elif s[i] == ')':
                    if not st or st[-1] != '(':
                        return False
                    st.pop(-1)
                else:
                    v = is_valid(st, i + 1)
                    if v:
                        return True
                    st.append('(')
                    v = is_valid(st, i + 1)
                    if v:
                        return True
                    if not st:
                        return False
                    st[-1] = ')'
                    return is_valid(st, i+1)
            return not st

        if not s:
            return True
        return is_valid([], 0)


# print Solution().checkValidString("()")
# print Solution().checkValidString("*")
print Solution().checkValidString("(*))")
