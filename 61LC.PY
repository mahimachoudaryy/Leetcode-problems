# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Find length
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        k %= n

        def rotate(head, k):
            if k == 0:
                return head
            prev = None
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next
            curr.next = head
            prev.next = None
            return rotate(curr, k - 1)
        return rotate(head, k)
        ''' missed edge cases from 9 to 19 line chatgpt cheppindhi'''

            
