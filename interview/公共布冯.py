def get_int():
    return int(input().strip())


def get_arr():
    arr = input().strip().split(" ")
    res = []
    for i in arr:
        res.append(int(i))
    return res


n = get_int()
val1 = get_arr()

m = get_int()
val2 = get_arr()

i, j = 0, 0

while i < n and j < m:
    if val1[i] == val2[j]:
        print(val1[i], end=" ")
        i+=1
        j+=1
    elif val1[i] > val2[j]:
        i += 1
    else:
        j += 1
