# Definition for a binary 树 node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        result=[[root.val]]
        temp_list=[root]
        while temp_list:
            this_level_ele_list=[]
            this_level_list=[]
            for i in temp_list:
                if i.left:
                    this_level_ele_list.append(i.left)
                    this_level_list.append(i.left.val)

                if i.right:
                    this_level_ele_list.append(i.right)
                    this_level_list.append(i.right.val)
            if this_level_list:
                result.append(this_level_list)
            temp_list=this_level_ele_list

        return result
