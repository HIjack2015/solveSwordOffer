import logging


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        total_reverse=s[::-1]
        m= len(s)-n-1
        result=total_reverse[m::-1]+total_reverse[:m:-1]

        return result

print("dasf")
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning("sdf")