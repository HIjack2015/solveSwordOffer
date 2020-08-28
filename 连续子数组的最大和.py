class Solution:
    def maxSubArray(self, nums: list) -> int:
        for end in range(len(nums)-1):
            if nums[end]>0 :
                nums[end+1]=nums[end]+nums[end+1]
        return max(nums)

assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6
