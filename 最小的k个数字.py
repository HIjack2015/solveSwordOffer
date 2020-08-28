import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(arr,k)