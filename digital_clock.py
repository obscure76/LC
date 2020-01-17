class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = set()

        def spl(t):
            hour = t >> 6
            minu = t & 63
            # print bin(t), hour, minu
            if hour < 12 and minu < 60:
                res.add(str(hour) + ":" + "%02d" % minu)

        def comb(x, total):
            if x == 0:
                spl(total)
                return
            for i in xrange(10):
                pv = total & 1 << i
                if pv:
                    continue
                total |= 1 << i
                comb(x - 1, total)
                total &= ~(1 << i)

        comb(num, 0)
        return list(res)




exp = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]

print sorted(Solution().readBinaryWatch(2))
print exp
