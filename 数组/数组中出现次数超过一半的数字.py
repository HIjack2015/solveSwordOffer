class Solution:
    def majorityElement(self, nums: list) -> int:
        may_be_answer=nums[0]
        show_count=0
        for i in nums:
            if show_count==0:
                may_be_answer=i

            if may_be_answer==i:
                show_count+=1
            else:
                show_count-=1
        return may_be_answer

assert Solution().majorityElement([1,2,1,2,1])==1

