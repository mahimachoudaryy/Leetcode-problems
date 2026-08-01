class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = 0
        while curr:
            c += 1
            curr = curr.next
        
        if n == c:
            return head.next
    
        curr = head
        for _ in range(c - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        
        return head
