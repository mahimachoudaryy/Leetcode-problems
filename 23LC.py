# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            temp=i
            while temp:
                arr.append(temp.val)
                temp=temp.next
        arr.sort()
        head=None
        tail=None
        for i in arr:
            newnode=ListNode(i)
            if head==None:
                head=newnode
                tail=newnode
            else:
                tail.next=newnode
                tail=newnode
        return head


