from typing import List

from collections import Counter
class UF:
    def __init__(self, n):
        self.uf = [-1] * n
    def find(self, idx):
        if self.uf[idx] == -1:
            return idx
        return self.find(self.uf[idx])
    def union(self, idx1, idx2):
        f1 = self.find(idx1)
        f2 = self.find(idx2)
        if f1 != f2: self.uf[f2] = f1
    def result(self):
        return Counter(self.uf)[-1]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UF(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.result()
result=Solution().countComponents(5,[[0, 1], [1, 2], [3, 4]])
print(str(result))
assert result==2