# coding=utf-8
import sys

result = 0


def get(x, y, z):
    global  result
    print("{}  {}  {}".format(x,y,z))
    # 判断包括两个0
    ele=[x,y,z]
    sum=x+y+z
    for i in ele:
        if i==sum:
            return
    if sum==2:
        return

    mineEle= min([x ,y ,z])

    result=result+mineEle
    x=x-mineEle
    y=y-mineEle
    z=z-mineEle

    sortedList= sorted([x,y,z])[::-1]
    x=sortedList[0]
    y=sortedList[1]
    a=(x-z)//3
    b=(y-z)//2

    if a>b:
        z =a
    else:
        z=b
    get(x-2*z,y-z,z)

get(20,15,9)
print(str(result))
