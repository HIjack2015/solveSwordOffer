class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        to_deal=head
        prev=None

        while to_deal is not None:
            to_deal_next=to_deal.next

            to_deal.next=prev
            prev=to_deal

            to_deal=to_deal_next

        return prev