# Definition for a binary 树 node
from 树.test import TreeNode, Tree


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        def recur(left,right):

            if not left and not right:
                return True
            if not left or not right or left.val!=right.val:
                return False
            return recur(left.right,right.left) and recur(left.left,right.right)
        return  recur(root.left,root.right) if root else True