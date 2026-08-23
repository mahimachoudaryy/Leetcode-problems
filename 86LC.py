# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        temp=head
        while temp:
            if temp.val < x:
                arr1.append(temp.val)
            else:
                arr2.append(temp.val)
            temp=temp.next
        head=None
        tail=None
        for i in (arr1+arr2):
            node=ListNode(i)
            if head==None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=tail.next
        return head
