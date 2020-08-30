class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        r=0
        for i in range(0,n-1):
           r= (m+r)%(i)
        return r
