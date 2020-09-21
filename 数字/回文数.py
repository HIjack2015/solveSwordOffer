class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revert_no = 0
        while x > revert_no:
            revert_no = revert_no * 10 + x % 10
            x = x // 10
        return x == revert_no or x == revert_no // 10
