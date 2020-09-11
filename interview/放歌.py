def get_int():
    return int(input().strip())

def get_arr():
    arr=input().strip().split(" ")
    res=[]
    for i in arr:
        res.append(int(i))
    return res

def get_res():
    get_int()

    values=get_arr()
    pack=get_int()
    new_pack=pack-1

    may_be_set=set()
    may_be_set.add(0)
    values=sorted(values)
    max_value=values[-1]


    for index,value in enumerate(values):
            may_be_set2=set()
            for last_value in may_be_set:
                this_value=value+last_value
                if this_value==new_pack:
                    if index < len(values) - 1:
                        return this_value + max_value
                may_be_set2.add(this_value)
            may_be_set=may_be_set.union(may_be_set2)
    set_max=max(may_be_set)
    if set_max <=pack:
        return set_max
    for may_be_max in range(new_pack,0,-1):
        if may_be_max in may_be_set:
            return may_be_max+max_value
print(get_res())
