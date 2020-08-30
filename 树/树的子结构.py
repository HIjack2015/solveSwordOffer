class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        return self.inner_check(A,B)

    def inner_check(self, A: TreeNode, B: TreeNode) -> bool:
        def this_is_same(A: TreeNode, B: TreeNode):
            if not B:return True
            if not A:return False
            if A.val !=B.val:return False
            return this_is_same(A.left,B.left) and this_is_same(A.right,B.right)
        if not A or not B:
            return False
        if this_is_same(A,B):
            return True

        sub_contains=self.inner_check(A.left,B) or self.inner_check(A.right,B)
        return sub_contains
    