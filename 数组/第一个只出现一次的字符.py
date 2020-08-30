import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        count_dict= collections.OrderedDict()
        for c in s:
            if c in count_dict.keys():
                count_dict[c]=False
            else:
                count_dict[c]=True
        for i in count_dict.keys():
            if count_dict[i]:
                return i
        return " "