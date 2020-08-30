# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        first_node=head
        second_node=head
        for i in range(0,k):
            second_node=second_node.next

        while second_node is not None:
            first_node=first_node.next
            second_node=second_node.next
        return first_node.val
