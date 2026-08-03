# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        temp = head

        while temp:
            ans.append(temp.val)
            temp = temp.next

        arr = sorted(ans)

        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next

        return head
