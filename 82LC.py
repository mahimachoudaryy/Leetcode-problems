# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        temp=head
        while temp:
            if temp.val in d:
                d[temp.val]+=1
            else:
                d[temp.val]=1
            temp=temp.next
        head = None
        tail = None

        for i in d:
            if d[i] == 1:
                node = ListNode(i)

                if head is None:
                    head = node
                    tail = node
                else:
                    tail.next = node
                    tail = node

        return head
