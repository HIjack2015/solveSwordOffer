
import  copy
class 砝码状态类:
    '''
    这个类表示当前可用的所有砝码以及如何达到当前的状态,
    '''

    def __init__(self, 做了什么, 上次砝码状态, 新增的砝码):
        if not 上次砝码状态:
            self.砝码合集 = 新增的砝码
            self.做了什么 = "初始化呢"
            self.行动步数 = 0
            self.剩余米=米的重量+sum(砝码们)-sum(self.砝码合集)
        else:
            self.砝码合集 =copy.copy(上次砝码状态.砝码合集)
            self.砝码合集.append(新增的砝码)
            self.做了什么 = 上次砝码状态.做了什么 +"\n"+ 做了什么
            self.行动步数 = 上次砝码状态.行动步数 + 1
            self.剩余米 = 米的重量 +sum(砝码们)- sum(self.砝码合集)

        self.新增的砝码=新增的砝码
    def sum(self):
        return sum(self.砝码合集)
    def __hash__(self):
        return self.做了什么.__hash__()

    def copy(self):

        return copy.deepcopy(self)

    def 卧槽成功了(self):
        if self.新增的砝码 in 目标重量:
            print("恭喜这个逼\n")
            print("共行动{}".format(self.行动步数))
            print("路径为：")
            print("砝码"+str(self.砝码合集))
            print(self.做了什么)

            return True
        else:
            return False

    def not_bad(self):
        return sum(self.砝码合集)< 米的重量+sum(砝码们) and self.新增的砝码>0


砝码们=[2,7]
米的重量=150
目标重量={90,米的重量-90}

当前砝码状态=砝码状态类("初始化",None,砝码们)
状态合集=[当前砝码状态]


def 根据砝码状态拿到下一砝码状态(砝码状态:砝码状态类):
    能秤的新重量合集= {0}

    新的砝码状态合集 = []
    新重量_解释=dict()
    新重量_解释[0]=""

    # 对于每个砝码,有不使用(0),放左边(*1),放右边(* -1)三种可能
    for 砝码 in 砝码状态.砝码合集:
        临时能秤的新重量合集=copy.copy(能秤的新重量合集)

        for 临时新重量 in 能秤的新重量合集:
            当前重量=临时新重量 + 砝码


            解释=新重量_解释[临时新重量]+" "+"左边放上砝码{} 秤出 {}".format(砝码,当前重量)
            新重量_解释[当前重量]=解释
            临时能秤的新重量合集.add(当前重量)
            新的砝码状态 = 砝码状态类(新重量_解释[临时新重量]+" "+解释, 砝码状态, 当前重量)
            新的砝码状态合集.append(新的砝码状态)


            当前重量 = 临时新重量 - 砝码


            解释 = 新重量_解释[临时新重量]+" "+"右边放上砝码{} 秤出 {}".format(砝码, 当前重量)
            新重量_解释[当前重量] = 解释
            临时能秤的新重量合集.add(当前重量)
            新的砝码状态 = 砝码状态类(新重量_解释[临时新重量]+" "+解释, 砝码状态, 当前重量)
            新的砝码状态合集.append(新的砝码状态)


        能秤的新重量合集=能秤的新重量合集.union(临时能秤的新重量合集)

    新的砝码状态合集2=[]
    for 新的砝码状态 in 新的砝码状态合集:
        if 新的砝码状态.新增的砝码>0:
            新的砝码状态合集2.append(新的砝码状态)
    新的砝码状态合集=新的砝码状态合集2

    加米后能秤的新重量合集=set()

    for  新的砝码状态 in  新的砝码状态合集:
        剩余米=新的砝码状态.剩余米
        能秤的新重量=新的砝码状态.新增的砝码

        if (剩余米 + 2*能秤的新重量)%2==0:  #暂且不考虑小数点
            新重量=(剩余米 + 2*能秤的新重量)/2
            加米后能秤的新重量合集.add(新重量)
            prefix_desc=新重量_解释[能秤的新重量] if 能秤的新重量 in 新重量_解释 else ""
            新状态=砝码状态类(prefix_desc +" "+"用重量{}加米秤出{}".format(能秤的新重量,新重量), 砝码状态, 新重量)
            新状态2=砝码状态类( prefix_desc+" "+"用重量{}加米 剩下部分秤出{}".format(能秤的新重量,剩余米-新重量), 砝码状态, 剩余米-新重量)

            新的砝码状态合集.append(新状态)
            新的砝码状态合集.append(新状态2)
    新的砝码状态合集2=[]
    for 新的砝码状态 in 新的砝码状态合集:
        if 新的砝码状态.新增的砝码>0 and 新的砝码状态.not_bad():
            新的砝码状态合集2.append(新的砝码状态)
    for 状态 in 新的砝码状态合集2:
        if 状态.卧槽成功了():
            return None
    return 新的砝码状态合集2


while True:
    新的状态合集=[]
    for  砝码状态 in 状态合集:
        当前状态所产生的状态合集 = 根据砝码状态拿到下一砝码状态(砝码状态)
        if  not 当前状态所产生的状态合集:
            exit()
        for 新状态 in 当前状态所产生的状态合集 :

            新的状态合集.append(新状态)
    状态合集=新的状态合集



