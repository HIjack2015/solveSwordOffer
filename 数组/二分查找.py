class Solution:
    def search(self, nums: [int], target: int) -> int:
        left,right=0,len(nums)-1
        while(left<=right):
            this_index=(left+right)//2
            this_ele=nums[this_index]
            if this_ele>target:
                right=this_index-1
            elif this_ele<target:
                left=this_index+1
            else:
                return this_index
        return -1


# Solution().search([-1,0,3,5,9,12],2)