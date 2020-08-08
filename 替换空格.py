class Solution:
    def replaceSpace(self, s: str) -> str:
        count_space=0
        for i in s:
            if i ==' ':
                count_space=count_space+1
        s_arr=[*s]
        last=len(s)
        new_arr =s_arr+ [None] * (count_space*2)
        for i in range(len(s)-1,-1,-1):
            if s_arr[i]==' ':
                index=i
                new_arr[count_space * 2 + i] = '0'
                new_arr[count_space * 2 + i-1] = '2'
                new_arr[count_space * 2 + i-2] = '%'

                for i in range(index+1, last):
                    new_arr[count_space * 2 + i] = s_arr[i]
                last = index
                count_space=count_space-1

        return "".join(new_arr)

print(Solution().replaceSpace("sdf asdf sdf"))