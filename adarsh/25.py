# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Insights from comments in
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11653/Python-recursive-and-iterative-solutions-with-comments
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
from typing import Optional


class ListNode:
    """
    Definition for singly-linked list
    """

    def __init__(
            self,
            val: int = 0,
            next=None,
    ):
        self.val = val
        self.next = next


def reverse_k_group(
        head: Optional[ListNode],
        k: int = 2,
) -> Optional[ListNode]:
    """
    Reverses the nodes of head k at a time and returns that linked list
    Algorithm: Given the head node of a linked list, check if there are at least k nodes in the linked list. If there
    isn’t, return the head node. If there is, then reverse k nodes (using standard linked list reversal), and call the
    function recursively by passing in the node after the kth node as the input parameter. When the recursive call
    returns, connect the current head node (which is the last node in the current k-group) to the return value. This
    will connect the tail of the current k-group to the head of the next k-group. At the end of each recursion, return
    the head of the reversed linked list.
    Time complexity: O(n), where n is the number of nodes in the input list.
    Space complexity: O(n/k), as recursion will be called n/k times. As mentioned, k is the number of nodes in a group
    that need to be reversed.

    :param head: Linked list
    :param k: Number of nodes in head to reverse at a time
    :return: modified linked list
    """
    # make sure there is a k-sized group in head
    curr_node = head
    for _ in range(k):
        if not curr_node:
            return head
        curr_node = curr_node.next

    # prev_head holds head of the previously modified nodes
    # curr_node does the heavy lifting
    prev_head, curr_node = None, head
    for _ in range(k):
        # next_node holds head of yet to be modified nodes
        next_node = curr_node.next
        # reverse the link between these nodes
        curr_node.next = prev_head
        # move pointers forward
        prev_head = curr_node
        curr_node = next_node

    # current k-group is reversed
    # connect it to head of next k-group
    head.next = reverse_k_group(curr_node, k)
    return prev_head
