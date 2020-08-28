class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target: j -= 1
            elif s < target: i += 1
            else: return [nums[i], nums[j]]
        return []