# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
# sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root. 
# The path sum of a path is the sum of the node's values in the path
# Given the root of a binary tree, return the maximum path sum of any non-empty path

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# This function returns overall maximum path sum in 'res'
# And returns max path sum going through root
def findMaxUtil(root) -> int:
    # Base Case
    if root is None:
        return 0
    # l and r store maximum path sum going through left
    # and right child of root respectively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)
    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.data, root.data)
    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l+r+ root.data)
    # Static variable to store the changes
    # Store the maximum result
    findMaxUtil.res = max(findMaxUtil.res, max_top)
    return max_single
 
# Return maximum path sum in tree with given root
def findMaxSum(root) -> int:
    # Initialize result
    findMaxUtil.res = float("-inf")
    # Compute and return result
    findMaxUtil(root)
