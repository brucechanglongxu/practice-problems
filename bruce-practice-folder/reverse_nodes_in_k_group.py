class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
class ListNode:
    """
    Our definition for our linked list data structure
    with one node set to a zero value, not pointing to another node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None
        
class Solution:
    """
    Main function for reversing k-nodes within our linked list defined, 
    implementation of a recursive solution. 
    """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverseKGroup(next, k)
        # prev is new head of the input list
        return prev
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

