# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    """
    Class for Reverse Nodes in k-Group (#25)
    https://leetcode.com/problems/reverse-nodes-in-k-group/
    """
    def reverse_k_group(self, 
                      head: Optional[ListNode], 
                      k: int
                     ) -> Optional[ListNode]:
        """
        Returns a linked list after reversing the list k nodes at a time
        We begin by adding each of the nodes in that particular order into a list called nodes. As soon as the number of added
        nodes is k, we add the nodes backwards, starting from the kth node until the 1st node into a linked list. We then 
        consider the remaining (n - k) nodes in the original linked list and repeat the same process by adding k nodes repeatedly 
        until we have less than k nodes left. The remaining nodes (less than k nodes) are added to the linked list in the same 
        order, and we return this linked list.
        
        Time complexity: O(n) [where n is the length of head]
        Space complexity: O(n) [where n is the length of head]
   
        :param head: the inputted linked list 
        :param k: the number of nodes to reverse at a time
        :return: the modified version of the original linked list
        """
        
        # a is an empty linked list which we define as a copy of the head linked list
        a = ListNode()
        a.next = head 
        
        # we create copies to prevent editing the original linked lists
        prev = a
        curr = head
         
        # we save all the nodes in head
        nodes = []
        while curr:
            # we save the nodes in the list until it's of length k at which point we need to reverse the entire list
            nodes.append(curr)
            curr = curr.next
            # as soon as there are k nodes in the list, we can start adding them to the linked list prev in reverse order
            if len(nodes) == k:
                while nodes:
                    # we add the last element first and remove it from our list
                    prev.next = nodes[-1]
                    nodes = nodes[:-1]
                    # we then iterate to the next node in the list to avoid overwriting the same node
                    prev = prev.next
                    
        # after we've removed the sets of k nodes, we just add the rest of the nodes in head to prev
        # the remaining nodes are already in the list nodes from the above loop but didn't get added to the prev linked list since it wasn't of length k yet
        while nodes:
            # in this case, we can start from the first element since they don't have to be reversed
            prev.next = nodes[0]
            # once we add the particular node, we can remove it from the list
            nodes = nodes[1:]
            prev = prev.next
        prev.next = None
        
        # since we formerly set prev to be a, editing prev changed a
        # a is defined from the very first node, unlike prev - since we iterated through it (prev = prev.next)
        return a.next
