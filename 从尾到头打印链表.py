# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list:
        result_list=list()
        node=head
        while node is not None:
            result_list.append(node.val)
            node=node.next
        result_list.reverse()
        return result_list
