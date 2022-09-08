# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    """
    Class for Reverse Nodes in k-Group (#25)
    # https://leetcode.com/problems/reverse-nodes-in-k-group/
    """
    def reverseKGroup(self, head, k):
        """
        Returns a linked list after reversing the list k nodes at a time
        
        Parameters
        ----------
        head : List
            the inputted linked list 
        k : int
            k represents the number of nodes to reverse at a time
            
        Return
        ------
        a : List
            the modified version of the original linked list
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
