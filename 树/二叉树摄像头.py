class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        not_in_monitor,in_monitor,has_monitor=-1,0,1

        self.res=0
        def dfs(node:TreeNode):

            if not node:
                return in_monitor
            left,right=dfs(node.left),dfs(node.right)
            if left==not_in_monitor or right==not_in_monitor:
                self.res+=1
                return has_monitor
            if left==has_monitor or right==has_monitor:
                return in_monitor
            return not_in_monitor

        i= dfs(root)
        if i==not_in_monitor:
            return self.res+1
        return self.res
