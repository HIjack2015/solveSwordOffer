from  typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        heights=[0]+heights+[0]
        stack=[0]

        for i in range(1,len(heights)):
            while heights[i]<heights[stack[-1]]:
                current_height=heights[stack.pop()]
                width=i-(stack[-1]+1)
                max_area=max(max_area,width*current_height)

            stack.append(i)


        return max_area



res = Solution().largestRectangleArea([2,1,5,6,2,3])
print(res)
