# 50 5
# 2 1 2
# 5 10 11 12 13 14
# 2 0 1
# 2 49 2
# 4 6 7 8 2

def get_arr():
    arr=input().strip().split(" ")
    res=[]
    for i in arr:
        res.append(int(i))
    return res

def get_2_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    return i,j

n,m=get_2_int()
arrs=[]
first_set=None
for i in range(m):
    this_set=set(get_arr()[1:])
    if 0 in this_set:
        first_set=this_set
    else:
        arrs.append(this_set)

known_set=set()
known_set=known_set.union(first_set)
while True:
    new_known_set=set()
    for team in arrs:
        for ele in team:
            if ele in known_set:
                new_known_set= new_known_set.union(team)
                break

    after_this_know=known_set.union(new_known_set)
    if known_set==after_this_know:
        break
    known_set=after_this_know
print(str(len(known_set)))
