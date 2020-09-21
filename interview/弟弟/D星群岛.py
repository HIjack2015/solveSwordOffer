def get_3_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    k=int(arr[2])
    return i,j,k
pre = {}
def find(x):
    r = x
    while pre[r] != r:
        r = pre[r]
    i = x
    while i != r:  # 路径压缩，平衡树层次的效果
        j = pre[i]
        pre[i] = j
        i = j
    return r


def join(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        # root = min(fx, fy)  # 平衡树的层次的效果
        # pre[fx] = root
        # pre[fy] = root
        pre[fx] = fy


def judge(n, edges):
    '''
    判断是否连通
    :param n: 节点数
    :param edges: 边的集合
    :return: 是否连通
    '''

    for i in range(n):
        pre[i] = i
    for i in range(len(edges)):
        join(edges[i][0], edges[i][1])
    group = 0
    for i in range(n):
        if pre[i] == i:
            group += 1
    if group == 1:
        return True
    else:
        return False



group_count= int(input())


data_groups=[]
data_group_n=[]
for group_idx in range(group_count):
    this_pic=[]
    n,m,k=get_3_int()
    data_group_n.append(n)

    for _ in range(0,m):
        island1,island2,cost=get_3_int()
        if cost<k:
            this_pic.append([island1-1,island2-1])
    data_groups.append(this_pic)




def can_build(n,ele:[]):
    return judge(n,ele)



for idx,ele in enumerate(data_groups):
    n=data_group_n[idx]
    pre={}
    if can_build(n,ele):
        print("Yes")
    else:
        print("No")

