a=[76,45,88,21,94,77,17]
res =0

for i in range(-100,100):
    for j in range(-100,100):
        if i+j<6 and 3*i-j+6>0 and i-3*j<6:
            res+=1
print(str(res))
