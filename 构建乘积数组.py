from operator import mul
class Solution:
    def constructArr(self, a: list) -> list:
        b=[1]*len(a)
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1] # 下三角
        temp=1
        for i in range(len(a)-2,-1,-1):
            temp*=a[i+1]
            b[i]*=temp
        return b

print(Solution().constructArr([1,2,3,4,5]))