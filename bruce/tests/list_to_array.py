class node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# Function to add a new node
# to the Linked List
def add(data):
  
    newnode = node(0)
    newnode.data = data
    newnode.next = None
    return newnode
  
# Function to print the array contents
def printArr(a, n):
  
    i = 0
    while(i < n):
        print (a[i], end = " ")
        i = i + 1
  
# Function to return the length
# of the Linked List
def findlength( head):
  
    curr = head
    cnt = 0
    while (curr != None):
      
        cnt = cnt + 1
        curr = curr.next
      
    return cnt
  
# Function to convert the
# Linked List to an array
def list_to_array(head):
  
    # Find the length of the
    # given linked list
    len1 = findlength(head)
  
    # Create an array of the
    # required length
    arr = []
  
    index = 0
    curr = head
  
    # Traverse the Linked List and add the
    # elements to the array one by one
    while (curr != None): 
        arr.append( curr.data)
        curr = curr.next
      
    # Print the created array
    printArr(arr, len1)
