# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along this path is equal to targetSum. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def parentPath2(root, sum):
            if not root:
                return 0
            if (root.val == sum):
                return 1 + parentPath2(root.left, sum - root.val) + parentPath2(root.right, sum - root.val)
            else:
                return parentPath2(root.left, sum - root.val) + parentPath2(root.right, sum - root.val)
        
        sum = targetSum
        # Appropriate recursive call 
        return parentPath2(root, sum) + parentPath2(root.left, sum) + parentPath2(root.right, sum)
