def get_2_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    return i,j
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def is_leaf(self):
        return self.left==None and self.right==None

n,m=get_2_int()

node_dict=dict() #key id ，value node
for i in range(m):
     eles=input().strip().split(" ")
     id=int(eles[0])
     child_node_id=int(eles[2])

     if not id in node_dict:
         node_dict[id]=TreeNode(id)

     if not child_node_id in node_dict:
         node_dict[child_node_id]=TreeNode(child_node_id)

     if eles[1]=="left":
         node_dict[id].left=node_dict[child_node_id]
     else:
         node_dict[id].right = node_dict[child_node_id]
result=0

def check(node:TreeNode):
    global result
    if not  node :
        return False
    if node.left and node.right and node.left.is_leaf() and node.right.is_leaf():
        result+=1
    check(node.left)
    check(node.right)
check(node_dict[1])
print(str(result))

