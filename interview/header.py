def get_2_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    return i,j

def get_3_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    k=int(arr[1])
    return i,j,k

def  print_arr(arr:[[]]):
    row_count=len(arr)
    col_count=len(arr[0])
    for row in range(row_count):
        for col in range(col_count):
            e = arr[row][col]
            if col < col_count - 1:
                print(str(e), end=" ")
            else:
                print(str(e), end="")
        if row < row_count - 1:
            print("")