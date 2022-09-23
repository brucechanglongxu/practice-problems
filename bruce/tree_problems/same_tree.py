# Given the roots of two binary trees P and Q, write a function to return whether they are structurally the same or not.

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Given two trees, return true if they are structurally
# identical
def identicalTrees(a, b):
    # 1. Both empty
    if a is None and b is None:
        return True
    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right))
    # 3. one empty, one not -- false
    return False
