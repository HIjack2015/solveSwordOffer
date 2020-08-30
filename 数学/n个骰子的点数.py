class Solution:
    def conv(self, p):
        c = 1 / 6
        length = len(p)
        res = [0] * (length + 5)
        for i in range(6):
            res[i] = res[i - 1] + p[i] * c
        for i in range(6, length):
            res[i] = res[i - 1] + (p[i] - p[i - 6]) * c
        for i in range(length, length + 5):
            res[i] = res[i - 1] - p[i - 6] * c
        return res


    def twoSum(self, n: int) -> list:
        res = [1 / 6] * 6
        for i in range(1, n):
            res = self.conv(res)
        return res