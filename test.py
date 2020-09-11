import sys

line0 = sys.stdin.readline().strip()
N = int(line0)


def get_ele(x, y):
    global N
    n = N
    if x < N / 2 and y < n / 2:
        if x < y:
            return 2
        else:
            return 3
    elif x < n / 2 and y >= n / 2:
        if x + y < n - 1:
            return 1
        else:
            return 8
    elif x >= n / 2 and y < n / 2:
        if x + y < n - 1:
            return 4
        else:
            return 5
    else:
        if x > y:
            return 6
        else:
            return 7

def inmi(x,y):
    global N
    if (N%2!=0):
        if x==N//2 or y==N//2:
            return True
    if x==y or x+y==N-1:
        return True
    return False
eles = [[0 for x in range(N)] for y in range(N)]
for i in range(N):
    for j in range(N):
        if inmi(i,j):
            print("0", end="")
        else:
            print(get_ele(i,j ), end="")
        if j!=N-1:
            print(" ",end="")
    if i!=N-1:
        print("")
