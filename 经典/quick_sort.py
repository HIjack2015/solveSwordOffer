arr=[5,7,8,1,2]

def partition(begin,end):
    pivot=begin
    for i in range(begin+1,end+1):
        if arr[i]<=arr[begin]:
            pivot+=1
            arr[i],arr[pivot]=arr[pivot],arr[i]
            print(arr)
    arr[pivot],arr[begin]=arr[begin],arr[pivot]
    print(arr)
    print("")
    return pivot


def quick_sort(begin=0,end=len(arr)-1):
    if begin>=end:
        return
    pivot_postion= partition(begin,end)
    quick_sort(begin,pivot_postion-1)
    quick_sort(pivot_postion+1,end)


quick_sort()
print(arr)