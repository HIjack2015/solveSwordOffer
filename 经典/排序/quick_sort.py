arr=[5,7,8,1,2,233216,118,328,2]

def swap(i,j):
    arr[i],arr[j]=arr[j],arr[i]

def partition(start, end):

    pivot_ele=arr[start]
    current_pivot=start
    for i in range(start+1,end+1):
        if arr[i]<pivot_ele:
            current_pivot += 1
            swap(i,current_pivot)


    swap(current_pivot,start)

    return current_pivot


def quick_sort(start=0,end=len(arr)-1):
    if start>=end:
        return

    pivot=partition(start,end)

    quick_sort(start,pivot-1)
    quick_sort(pivot+1,end)

    return

quick_sort()
print(arr)