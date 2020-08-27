class Solution:
    def findContinuousSequence(self, target: int) ->list:
        def get_sub(target,num_count):
            target_是偶数=(target%2==0)
            位移=int(num_count/2)
            result=list()
            中间值=int(target/num_count)
            恰好整除=(target%num_count==0)


            if 恰好整除:
                if num_count%2==0:
                    return None
                for i in range(中间值-位移,中间值+位移+1):
                    result.append(i)

            if not 恰好整除:
                if (中间值*2+1)*位移!=target:
                    return None
                for i in range(中间值-位移+1,中间值+位移+1):
                    result.append(i)
            for e in result:
                if e<1:
                    return None
            return result
        results=list()
        for i in range(target-1,1,-1):
            sub=get_sub(target,i)
            if sub is not None:
                results.append(sub)
        return results
print(Solution().findContinuousSequence(100))