def get_2_int():
    arr = input().strip().split(" ")
    i = int(arr[0])
    j = int(arr[1])
    return i, j




def  print_arr(arr:[]):

    for row in arr:
        print(row)

def check(arr, sub_arr_len):
    '''
    :param arr:
    :param end_line:  长度
    :return:
    '''
    if len(arr) % 2 != 0:  # 如果是奇数行
        return False
    j = sub_arr_len - 1
    temp_len=sub_arr_len //2
    for i in range(0,  temp_len):
        if arr[i] != arr[j]:
            return False
        j -= 1
    return True

n, m = get_2_int()  # n行，每行m个

arr = []
raw_arr=[]
for i in range(n):
    str_ele=input()
    eles = int(str_ele.replace(" ",""))
    arr.append(eles)
    raw_arr.append(str_ele)
need_check = True

sub_arr_len = 1
while need_check:
    need_check = check(arr, sub_arr_len)
    if not need_check:
        print_arr(raw_arr[0:sub_arr_len])
    else:
        sub_arr_len = sub_arr_len // 2
