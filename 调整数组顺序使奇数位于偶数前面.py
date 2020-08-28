
class Solution:
    def exchange(self, nums: list) -> list:
        def is_even(i):
            return i%2==0

        left,right=0,len(nums)-1
        while left<right:
            if not is_even(nums[left]): left+=1
            if is_even(nums[right]): right-=1
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right+=1
        return nums
