class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        bitmap=[0]*len(nums)

        for i in nums:
            if bitmap[i]!=0:
                return i
            else:
                bitmap[i]=1
