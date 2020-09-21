from collections import Counter
from typing import List

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
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
            uf=UF(2000)
            for edge in edges:
                n1=edge[0]
                n2=edge[1]
                if uf.find(n1)==uf.find(n2) and n1!=-1:
                    return edge
                uf.union(n1,n2)




