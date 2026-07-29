# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
                
                #why we did this is , bcz , we are not given the head only , so we need not traverse the entire list, and we should'nt delete it in the form of delete method , instead make the node same as nextnode and thats how the connection of previous and the current node happens

