class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        node=self
        while node is not None:
            print(node.val,end=" ")
            node=node.next

import copy
def gethead(x:list):
        node_list=list()
        for i in x:
            node_list.append(ListNode(i))

        for i in range(0,len(node_list)-1):
            node_list[i].next=node_list[i+1]
        return node_list[0]

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_head=None
        new_node=None
        while l1 is not None or l2 is not None:

            if l1 is None:
                if new_head is None:
                    new_head = copy.copy(l2)
                    new_node = new_head
                else:
                    new_node.next = copy.copy(l2)
                    new_node = new_node.next
                l2 = l2.next
            elif l2 is None:
                if new_head is None:
                    new_head = copy.copy(l1)
                    new_node = new_head
                else:
                    new_node.next = copy.copy(l1)
                    new_node = new_node.next
                l1 = l1.next

            elif  l1.val>l2.val :
                if new_head is None:
                    new_head = copy.copy(l2)
                    new_node = new_head
                else:
                    new_node.next = copy.copy(l2)
                    new_node = new_node.next
                l2 = l2.next

            elif  l2.val>=l1.val:
                if new_head is None:
                    new_head = copy.copy(l1)
                    new_node = new_head
                else:
                    new_node.next = copy.copy(l1)
                    new_node = new_node.next
                l1 = l1.next

        return new_head
