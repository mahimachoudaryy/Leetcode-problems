# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

        # dummy = ListNode(0) creates a temporary node before head.we created it bcz incase if we need to do it from the first node itself (i could'nt solve or understand from line 8 to 12)
