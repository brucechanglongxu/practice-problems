# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        a = head
        n = 1
        while (a.next):
            n += 1
            a = a.next
        if (k > n):
            return head
        
        prev = None
        curr = head
        
        for i in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        head.next = self.reverseKGroup(curr, k)
        return prev
