import functools


class Solution:
    def minNumber(self, nums: [int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

#
# 作者：jyd
# 链接：https: // leetcode - cn.com / problems / ba - shu - zu - pai - cheng - zui - xiao - de - shu - lcof / solution / mian - shi - ti - 45 - ba - shu - zu - pai - cheng - zui - xiao - de - s - 4 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。