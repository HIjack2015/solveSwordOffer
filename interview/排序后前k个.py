import random
import string
from collections import Counter

# for i in range(1000):
#     print(''.join(random.choices(string.ascii_letters + string.digits, k=3)))
#


def get_2_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    return i,j


N,K=get_2_int()
arr=[]
for i in range(0,N):
    arr.append(input().strip())
arr=sorted(arr)
count_dict=Counter(arr)



mostK= count_dict.most_common(K)
for value,count in mostK:
    print("{} {}".format(value,count))
for k in count_dict.keys():
    count_dict[k]=-count_dict[k]
mostK= count_dict.most_common(K)
for value,count in mostK:
    print("{} {}".format(value,-count))


