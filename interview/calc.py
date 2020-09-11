def calculate( s: str) -> int:
    ssssssssssss = []
    oooooooooooo = []
    i = 0
    priorty = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        if '0' <= s[i] <= '9':
            j = i
            while i + 1 < len(s) and '0' <= s[i + 1] <= '9':
                i += 1
            num = int(s[j:i + 1])
            ssssssssssss.append(num)
        elif s[i] == '(':
            oooooooooooo.append(s[i])
        elif s[i] == ')':
            while oooooooooooo[-1] != '(':
                opt = oooooooooooo.pop()
                A = ssssssssssss.pop()
                B = ssssssssssss.pop()
                res = cccccccccccccc(A, B, opt)
                ssssssssssss.append(res)
            oooooooooooo.pop()
        else:
            while oooooooooooo and priorty[oooooooooooo[-1]] >= priorty[s[i]]:
                opt = oooooooooooo.pop()
                A = ssssssssssss.pop()
                B = ssssssssssss.pop()
                res = cccccccccccccc(A, B, opt)
                ssssssssssss.append(res)
            oooooooooooo.append(s[i])
        i += 1

    while oooooooooooo:
        opt = oooooooooooo.pop()
        A = ssssssssssss.pop()
        B = ssssssssssss.pop()
        res = cccccccccccccc(A, B, opt)
        ssssssssssss.append(res)
    return ssssssssssss[-1]


def cccccccccccccc(n111111111, n22222222222, opt):
    if opt == '+':
        return int(n111111111) + int(n22222222222)
    elif opt == '-':
        return int(n22222222222) - int(n111111111)
    elif opt == '*':
        return int(n22222222222) * int(n111111111)
    elif opt == '/':
        return int(n22222222222) // int(n111111111)




input_str = str(input()).strip()
print(str(calculate(input_str)))