# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slw = head
        fst = head
        while fst and fst.next:
            slw = slw.next
            fst = fst.next.next
        slw = slw.next
        temp = head
        while temp:
            if temp.next == slw:
                temp.next = None
                break
            temp = temp.next
        prv = None
        cr = slw
        while cr:
            next = cr.next
            cr.next = prv
            prv = cr
            cr = next
        temp1 = head
        temp2 = prv
        while temp1 and temp2:
            next1 = temp1.next
            next2 = temp2.next
            temp1.next = temp2
            temp2.next = next1
            temp1 = next1
            temp2 = next2
        return
