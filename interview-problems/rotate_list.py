# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 1
        a = head
        if (head is None):
            return head
        while (a.next):    
            a = a.next
            n += 1
        # counts the number of nodes in the linked list
        
        if (k % n == 0): 
            return head
        k = k % n
        # ensures k is less than n to avoid repetition
        k = n - k
        # to rotate anti-clockwise rather than clockwise
        
        x = head
        count = 1 
        while(count < k and x is not None):
            x = x.next
            count += 1
        # x will point to the kth node
        NodeK = x
    
        while (x is not None and x.next is not None):
            x = x.next 
        # x is now the last node after the loop

        x.next = head 
        # changing the node after the last node to be head
        
        head = NodeK.next # changes the head to be the (k + 1)th node

        NodeK.next = None # the node after the kth node should be null

        return head
