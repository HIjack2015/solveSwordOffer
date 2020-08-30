# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        n1=head
        n2=head.next
        if n1.val==val:
            return n1.next
        while n2.val!=val:
            n1=n1.next
            n2=n2.next
        n1.next=n2.next
        return head

