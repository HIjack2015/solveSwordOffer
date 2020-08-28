# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 如果当前节点对应一颗平衡树，返回深度，如果不是，则返回-1
        def recur(node):
            if not node:
                return 0
            left_ok = recur(node.left)
            if left_ok == -1:
                return -1
            right_ok = recur(node.right)
            if right_ok == -1:
                return -1
            return max(left_ok, right_ok) + 1 if abs(left_ok - right_ok) < 2 else -1

        return recur(root) != -1
