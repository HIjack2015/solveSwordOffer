class Solution:

    def __init__(self):
        self.temp_result=dict()


    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        is_negtive=(n!=abs(n))
        n=abs(n)
        t=1
        b=n
        temp_x=x
        self.temp_result[1]=(temp_x)
        while t<=b/2:

            temp_x=temp_x*temp_x
            t = t * 2
            self.temp_result[t]=(temp_x)

        keys=list(self.temp_result.keys())
        keys.reverse()
        while t<b:

            for i in keys:
                if i<=b-t:

                    temp_x=self.temp_result[i]*temp_x
                    t=t+i
                    break
        if is_negtive:
            return 1/temp_x
        return temp_x

Solution().myPow(0.00001,2147483647)