class Solution:
    def isStraight(self, nums: list) -> bool:
        without0_list = list(filter(lambda i: i != 0, nums))
        if max(without0_list)-min(without0_list)>4:
            return False

        if len(without0_list)!=len(set(without0_list)):
            return False
        return True
assert  Solution().isStraight([0,0,1,2,3])