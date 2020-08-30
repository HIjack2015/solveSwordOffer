class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next_to_deal=head
        prev=None

        while next_to_deal is not None:
            to_deal_next=next_to_deal.next

            next_to_deal.next=prev
            prev=next_to_deal

            next_to_deal=to_deal_next

        return prev