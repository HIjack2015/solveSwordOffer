class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0: return (rem * 3) % p # = 3^(a+1) % p
        if b == 1: return (rem * 4) % p # = 3^a * 4 % p
        return (rem * 6) % p # = 3^(a+1) * 2  % p
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。