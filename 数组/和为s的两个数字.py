class Solution:
    # 有序两数
    def twoSum(self, nums: list, target: int) -> list:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target: j -= 1
            elif s < target: i += 1
            else: return [nums[i], nums[j]]
        return []
    # 无序两数
    def twoSum2(self, nums: [int], target: int) -> [int]:
        temp_dict = dict()
        for i, e in enumerate(nums):
            if target - e in temp_dict.keys():
                return [i,temp_dict[target-e]]
            else:
                temp_dict[e]=i