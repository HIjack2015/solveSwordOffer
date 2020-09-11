# 给定 3 件物品，物品的重量为 weight[]={1,3,1}，对应的价值为 value[]={15,30,20}。现挑选物品放入背包中，
# 假定背包能承受的最大重量 W 为 4，问应该如何选择装入背包中的物品，使得装入背包中物品的总价值最大？

# https://www.cnblogs.com/kkbill/p/12081172.html

weights=[1,3,1]
values=[15,30,20]
weights=weights
values=values
# TODO 边界判断有问题，暂时不管了
W=4
dp_value=[[0]*W]*len(values)
for row in range(1,len(values)):
    for column in range(W):
        weight,value=weights[row],values[row]
        if row>0:

            dont_need=dp_value[row-1][column]

            if column-weight<0:
                need_this=-1111111
            else:
                need_this=value+dp_value[row-1][column-weight]
            dp_value[row][column]=max(dont_need,need_this)
            print(" set  row  {} column {} to {}".format(row,column,dp_value[row][column]))
        else:
            dp_value[row][column]=values[0]

    print("oneloop-=------------")
print(max(dp_value[-1]))