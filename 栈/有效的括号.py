class Solution:
    def isValid(self, s: str) -> bool:
        temp_stack=[]
        brace_dict={")":"(",
                    "}":"{",
                    "]":"["}
        for c in s:
            if c in brace_dict.values():
                temp_stack.append(c)
            if c in brace_dict.keys():
                if not temp_stack or  brace_dict[c]!=temp_stack[-1]:
                    return False
                else:
                    temp_stack.pop()
        if temp_stack:
                return False
        return True

