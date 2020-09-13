s = input().strip()
n = len(s)
res = 0


def helper(i, j):
    global res
    while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1
        if j-i>2:
            res += 1
for i in range(n):
        helper(i, i)
        helper(i, i + 1)


print(str(res))
