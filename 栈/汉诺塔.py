from typing import List


class Solution:

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:

        def move(n, A, B, C):
            if n == 1:
                C.append(A.pop())
                return
            else:
                move(n - 1, A, C, B)
                C.append(A.pop())
                move(n - 1, B, A, C)

        move(len(A),A,B,C)



C = []
A = [1, 0]
B = []
Solution().hanota(A,B,C)
print(C)


