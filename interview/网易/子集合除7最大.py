

eles=input().split(" ")

may_be_set=set()
may_be_set.add(0)

for i in eles:
    e=int(i)
    temp_set=set()
    for may_be_val in may_be_set:
        temp_set.add(may_be_val+e)
    may_be_set=may_be_set.union(temp_set)

not_ok=True
while not_ok:
    max_val=max(may_be_set)
    if max_val%7==0:
        print(str(max_val))
        not_ok=False
    else:
        may_be_set.remove(max_val)
