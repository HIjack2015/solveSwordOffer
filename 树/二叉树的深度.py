class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    max=0
    def check_node(self,depth,node:TreeNode):
        if node.left is not None:
            self.check_node(depth+1,node.left)
        if node.right is not None:
            self.check_node(depth+1,node.right)
        if depth>self.max:
            self.max=depth

        return
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.check_node(1,root)
        return self.max