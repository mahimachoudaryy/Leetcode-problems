# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        result=[]
        while(temp):
            if(temp.val!=temp.next.val):
                result.append(temp.val)
            temp=temp.next
        return result 

            
