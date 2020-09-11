xy= input().strip().split(" ")
x=int(xy[0])
y=int(xy[1])
commands=input()
for c in commands:
    if c=='L':
        x-=1
    if c=='R':
        x+=1
    if c=='U':
        y-=1
    if c=='D':
        y+=1
print(str(x)+" "+str(y) )
