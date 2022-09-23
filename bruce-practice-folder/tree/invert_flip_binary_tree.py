# Given the root of a binary tree, invert the tree, and return its root 

# Recursive Approach
class newNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

def invert(node):
  if (node == None):
    return
  else:
    temp = node
    # Recursive calls on left and right subtree 
    invert(node.left)
    invert(node.right)
    
    # Swap the pointers in this node
    temp = node.left
    node.left = node.right
    node.right = temp
    
# Print inOrder binary tree traversal    
def printTree(node):
  if (node == None):
    return
  printTree(node.left)
  print node.data
  printTree(node.right)  
