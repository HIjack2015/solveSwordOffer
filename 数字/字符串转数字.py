import re
class Solution:
    def isNumber(self, s: str) -> bool:
        if s and s.strip():
            return re.match("^[-+]?(\d+.?\d*|.\d+)([eE][+-]?\d+|\d+)?$", s.strip()) !=None