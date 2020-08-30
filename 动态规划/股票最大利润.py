class Solution:
    def maxProfit(self, prices: [int]) -> int:
      profit_list=[0]
      for i in range(1,len(prices)):

          current_price=prices[i]
          last_price=prices[i-1]
          profit_current_day=prices[i]-prices[i-1]
          profit_list.append(profit_current_day)
      print(profit_list)
      return self.maxSubArray(profit_list)
    def maxSubArray(self, nums: list) -> int:
        for end in range(len(nums)-1):
            if nums[end]>0 :
                nums[end+1]=nums[end]+nums[end+1]
        return max(nums)
assert 5== Solution().maxProfit([7,6,4,3,1])