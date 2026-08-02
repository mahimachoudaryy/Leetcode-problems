# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''  if not head or not head.next:
                return head 
            f=head
            s=head.next
            while f and s:
                t=s.next
                s.next=f
                f.next=t
                f=t
                s=f.next
            return f '''

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
