class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        slide_left=0
        slide_right=0
        slide_dict=dict() #key是ele ，value 是index

        temp_max=0

        for i,e in enumerate(s):
            if e in slide_dict:
                if slide_dict[e]>=slide_left:
                    temp_max=max(temp_max,slide_right-slide_left)
                    slide_left=slide_dict[e]+1

            slide_dict[e] = i
            slide_right+=1
        return max(temp_max,slide_right-slide_left)
print(Solution().lengthOfLongestSubstring("b"))


