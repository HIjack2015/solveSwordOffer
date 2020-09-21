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
    def in_same_set(self,idx1,idx2):
        f1 = self.find(idx1)
        f2 = self.find(idx2)
        return f1==f2

    def is_liantong(self):
        return len(Counter(self.uf)[-1])<3
    def has_circle(self):
        return len(Counter(self.uf)[-1])<3



class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        核心思路：
            如果有环，返回环中最后一个边
            如果入度为2，则先不把这个边放进去，如果
                是连通的，则返回这个边。
                如果不是连通的，则返回另一个边


        :param edges:
        :return:
        '''
        last_be_circle_edge=None
        end_node_2_edge_dict=dict()
        duplicate_edge=None

        uf=UF(1200)
        for edge in edges:
            start_node=edge[0]
            end_node=edge[1]

            if end_node in end_node_2_edge_dict:
                duplicate_edge=edge
                continue
            else:
                end_node_2_edge_dict[end_node]=edge
            if uf.in_same_set(start_node,end_node):
                last_be_circle_edge=edge
            uf.union(start_node,end_node)
        if duplicate_edge is None:
            return last_be_circle_edge
        has_circle=last_be_circle_edge is not None
        if has_circle:
            return end_node_2_edge_dict[duplicate_edge[1]]
        else:
            return duplicate_edge




Solution().findRedundantDirectedConnection([[1,2],[1,3],[2,3]])