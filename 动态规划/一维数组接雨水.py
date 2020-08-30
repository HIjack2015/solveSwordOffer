from  threading import Condition
class Solution:
    def trap(self, height: [int]) -> int:
        if not height:
            return 0

        stack = []
        result = 0

        for i, e in enumerate(height):
            while stack and e > height[stack[-1]]:
                min_ele_idx = stack.pop()
                if not stack:
                    break
                min_ele = height[min_ele_idx]
                left_wall_i= stack[-1]
                left_wall_h=height[left_wall_i]

                distance=i-left_wall_i-1
                bound_height=min(left_wall_h,e)-min_ele
                result+=distance*bound_height
            stack.append(i)

        return result


print(str(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])))
