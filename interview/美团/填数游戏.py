'''
小团和小美正在玩一个填数游戏，这个游戏是给一个等式，其中有一些数被挖掉了，你需要向其中填数字，使得等式成立。

比如 ___+12=34，那么横线填的一定是22

现在，这个游戏到了最后一关，这一关的等式很奇特：_+_+_+...+_=n

这里可以填任意多个正整数（甚至可能是1个），只要这些数的和等于n即可。

但是，有一个额外的限制，填入的所有数必须小于等于k，大于等于1，填入的数的最大值必须大于等于d。

请你计算，有多少个不同的等式满足这些限制。由于答案可能很大，请将答案mod(998244353)后输出。

'''
def get_3_int():
    arr=input().strip().split(" ")
    i=int(arr[0])
    j=int(arr[1])
    k=int(arr[2])
    return i,j,k

target_no,must_below_ele,max_value_must_over=get_3_int()

raw_arr=[1]
for e in range(2,target_no):
    this_count=0
    have_equal=False
    for i in range(1,e):
            first_ele=i
            second_ele=e-i
            if first_ele==second_ele:
                if have_equal:
                    continue
                have_equal=True


            if first_ele>must_below_ele or second_ele>must_below_ele:
                continue

            this_count+=raw_arr[first_ele-1]*raw_arr[second_ele-1]

    if e<must_below_ele:
        this_count+=1
    this_count = this_count % 998244353

    raw_arr.append(this_count)

print(raw_arr[target_no-1])