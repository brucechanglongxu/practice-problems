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
        # counts the number of nodes in the linked list
        n = 1
        a = head
        if (head is None):
            return head
        while (a.next):    
            a = a.next
            n += 1
        
        if (k % n == 0): 
            return head
        # ensures k is less than n to avoid repetition
        k = k % n
        # to rotate anti-clockwise rather than clockwise
        k = n - k
        
        # x will point to the kth node
        x = head
        count = 1 
        while(count < k and x is not None):
            x = x.next
            count += 1
        NodeK = x
    
        # x is now the last node after the loop
        while (x is not None and x.next is not None):
            x = x.next 

        # changing the node after the last node to be head
        x.next = head 

        # changes the head to be the (k + 1)th node
        head = NodeK.next 

        # the node after the kth node should be null
        NodeK.next = None 

        return head
