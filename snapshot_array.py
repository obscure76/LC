class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.l = [0] * length
        self.m = {}
        self.s = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.l[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.m[self.snap] = self.l[:]
        self.s += 1
        return self.s - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        return self.m[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
length = 3
obj = SnapshotArray(length)
index,val = 0,5
obj.set(index,val)
print type(obj)
param_2 = obj.snap()
index,val = 0,6
obj.set(index,val)
param_3 = obj.get(index,param_2)