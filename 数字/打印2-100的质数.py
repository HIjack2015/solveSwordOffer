def is_zhishu(ele):
    count = 0
    for i in range(2, ele + 1):
        if ele % i == 0:
            count += 1
    return count == 1


for ele in range(2, 101):
    if is_zhishu(ele):
        print(ele, end=" ")
