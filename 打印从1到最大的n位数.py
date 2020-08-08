class Solution:
    def printNumbers(self, n: int) -> list:
        current="1"
        result = list()
        while len(current)<=n:
            result.append(int(current))
            current=self.inc(current)

        return result

    def inc(self,input:str):
        size=len(input)
        input=[*input]

        for i in range(size-1,-1,-1):
            is9=input[i]=='9'
            input[i]=str(int(input[i])+1)[-1]
            if not is9:
                break
        if input[0]=='0':
            input.insert(0,"1")
        return "".join(input)
print(Solution().printNumbers(1))