from decimal import Decimal

import math
xy = input().strip().split(" ")
row_count = int(xy[0])
col_count = int(xy[1])

import  decimal

arr = []
for i in range(row_count):
    s = input().strip().split(" ")
    i_arr = []
    for e in s:
        i_arr.append(int(e))
    arr.append(i_arr)

for row in range(row_count):
    for col in range(col_count):
        e = arr[row][col]
        sum = e
        count = 1

        if row > 0:
            up = arr[row - 1][col]
            sum += up
            count += 1
        if row < row_count-1:
            down = arr[row + 1][col]
            sum += down
            count += 1
        if col > 0:
            left = arr[row][col-1]
            sum += left
            count += 1
        if col < col_count-1:
            right = arr[row][col+1]
            sum += right
            count += 1
        arr[row][col]=int(sum/count+0.5)

for row in range(row_count):
    for col in range(col_count):
        e = arr[row][col]
        if col<col_count-1:
            print(str(e),end=" ")
        else:
            print(str(e), end="")
    if row<row_count-1:
        print("")