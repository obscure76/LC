class Solution():
    def small_sum(self, s, m):
        if s == 0:
            return
        if s > 9 * m:
            print("Not possible")
            return
        res = [0 for _ in range(m)]
        s -= 1
        for i in range(m - 1, 0, -1):
            if s > 9:
                res[i] = 9
                s -= 9
            else:
                res[i] = s
                s = 0
                break
        res[0] = s + 1
        return "".join(str(x) for x in res)


print Solution().small_sum(9, 2)
