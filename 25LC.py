# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rec(head):
            temp = head
            for i in range(k):
                if temp is None:
                    return head
                temp = temp.next
            prv=None
            cr=head
            for i in range(k):
                    nxt=cr.next
                    cr.next=prv
                    prv=cr
                    cr=nxt
            rest=rec(cr)
            head.next=rest
            return prv
        return rec(head)
