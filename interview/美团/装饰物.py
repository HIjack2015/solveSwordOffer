def get_3_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    k=int(arr[2])
    return i,j,k

n,m,k=get_3_int() #n是数组长度，m是子数组长度，k是不能低于的值

arr=[]
eles= input().split(" ")
for e in eles:
    arr.append(int(e))

res_count=0
for i in range(0,len(arr)-m+1):
    sub_arr=arr[i:i+m]
    this_sub_ok=True
    for e in sub_arr:
        if e<k:
            this_sub_ok=False
    if this_sub_ok:
        res_count+=1
print(str(res_count))